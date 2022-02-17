import json
import os

from django.shortcuts import render, get_object_or_404
from django.conf import settings as conf_settings, settings
from mainapp.models import ProductCategory, Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from cartapp.models import CartItem

import random

# Create your views here.

def get_cart(user):
    if user.is_authenticated:
        return CartItem.objects.filter(user=user)
    else:
        return []

def get_random_good():
    # return random.choice(Product.objects.all())
    products = Product.objects.filter(is_active=True, category__is_active=True)
    # return random.sample(list(products), 1)[0]
    return random.choice(products)


def get_same_goods(random_product):
    products = list(Product.objects\
        .filter(is_active=True, category=random_product.category)\
        .exclude(pk=random_product.pk))
    random.shuffle(products)
    return products[:3]



def indexpage(request):
    page_title = 'главная'
    featured_goods = list(Product.objects.filter(is_active=True))
    random.shuffle(featured_goods)
    context = {
        "page_title": page_title,
        "cart_items": get_cart(request.user),
        "same_goods": featured_goods[:3],
        }
    return render(
        request, "mainapp/index.html", context=context
    )  # в пространстве имен mainapp


def products(request):
    """Показываем главную страницу категорий"""
    page_title = "каталог"
    links_menu_cat = ProductCategory.objects.filter(is_active=True)
    random_good = get_random_good()

    context = {
        "page_title": page_title,
        "links_menu_cat": links_menu_cat,
        "cart_items": get_cart(request.user),
        "product": random_good,
        "same_products": get_same_goods(random_good)
    }
    return render(request, "mainapp/products.html", context=context)


def contact(request):
    with open(os.path.join(settings.BASE_DIR, "json", "saveddata.json"), "r") as f:
        locations = json.load(f)
    cart_items = get_cart(request.user)

    context = {
        "page_title": "контакты",
        "locations": locations,
        "cart_items": cart_items,
    }
    return render(request, "mainapp/contact.html", context=context)


def category(request, pk=None, page=1):
    page_title = 'товары категории'
    links_menu_cat = ProductCategory.objects.filter(is_active=True)
    cart_items = get_cart(request.user)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(
                is_active=True, category__is_active=True
            ).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects\
                .filter(category__pk=pk, is_active=True, category__is_active=True)\
                .order_by("price")
            # products = Product.objects.filter(category=category)  # один вариант
            # products = category.product_set.all()  # второй вариант

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
            "page_title": page_title,
            "links_menu_cat": links_menu_cat,
            "products": products_paginator,
            "category": category,
            "primkey": pk,
            "cart_items": cart_items,
        }
        return render(request, "mainapp/products_detail.html", context=context)

    # random_product = get_random_good()
    # same_products = get_same_goods(random_product, 3)

    context = {
        "page_title": page_title,
        "links_menu_cat": links_menu_cat,
        # "random_product": random_product,
        # "same_products": same_products,
        "cart_items": cart_items,
        }
    return render(request, "mainapp/products.html", context=context)

def product(request, pk, slug):
    page_title = "Продукт"
    links_menu_cat = ProductCategory.objects.filter(is_active=True)

    product = get_object_or_404(Product, pk=pk)

    content = {
        "page_title": page_title,
        "links_menu_cat": links_menu_cat,
        "product": product,
        'cart_items': get_cart(request.user),
    }
    return render(request, "mainapp/product.html", content)
