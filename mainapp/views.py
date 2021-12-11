import json
import os

from django.shortcuts import render
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
    print(pk)
    # context={'title':'каталог',
    #          'primkey': pk}
    # return render(request, 'mainapp/products.html', context=context)
