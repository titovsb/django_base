import json
import os

from django.shortcuts import render, get_object_or_404
from django.conf import settings as conf_settings, settings
from mainapp.models import ProductCategory


# Create your views here.

def indexpage(request):
    context = {
        'page_title': 'главная'
        }
    return render(request, 'mainapp/index.html', context=context)  # в пространстве имен mainapp


def products(request):
    categories = ProductCategory.objects.all()

    context = {
        'page_title': 'каталог',
        'categories': categories,
        }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    with open(os.path.join(settings.BASE_DIR, 'json', 'saveddata.json'), 'r') as f:
        locations = json.load(f)
    context = {
        'page_title': 'контакты',
        'locations': locations,
        }
    return render(request, 'mainapp/contact.html', context=context)

def category(request, pk):
    if pk == 0:
        category = {'pk':0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        # products = Product.objects.filter(category=category)  # один вариант
        products = category.product_set.all()                   # второй вариант
    print(pk)
    context={'page_title':'товары категории',
             'primkey': pk}
    return render(request, 'mainapp/products.html', context=context)
