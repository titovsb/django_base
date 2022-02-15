import json
import os

from django.shortcuts import render, get_object_or_404
from django.conf import settings as conf_settings, settings
from mainapp.models import ProductCategory, Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def indexpage(request):
    context = {"page_title": "главная"}
    return render(
        request, "mainapp/index.html", context=context
    )  # в пространстве имен mainapp


def products(request):
    """Показываем главную страницу категорий"""
    links_menu_cat = ProductCategory.objects.filter(is_active=True)

    context = {
        "page_title": "каталог",
        "links_menu_cat": links_menu_cat,
    }
    return render(request, "mainapp/products.html", context=context)


def contact(request):
    with open(os.path.join(settings.BASE_DIR, "json", "saveddata.json"), "r") as f:
        locations = json.load(f)
    context = {
        "page_title": "контакты",
        "locations": locations,
    }
    return render(request, "mainapp/contact.html", context=context)


def category(request, pk=None, page=1):
    links_menu_cat = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(
                is_active=True, category__is_active=True
            ).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True
            ).order_by("price")

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
            "page_title": "товары категории",
            "links_menu_cat": links_menu_cat,
            "products": products_paginator,
            "category": category,
            "primkey": pk,
        }
        return render(request, "mainapp/products_detail.html", context=context)


def product(request, pk, slug):
    title = "Продукт"
    links_menu_cat = ProductCategory.objects.filter(is_active=True)

    product = get_object_or_404(Product, pk=pk)

    content = {
        "page_title": title,
        "links_menu_cat": links_menu_cat,
        "product": product,
        # 'basket': get_basket(request.user),
    }
    return render(request, "mainapp/product.html", content)
