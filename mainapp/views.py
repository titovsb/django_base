import json
import os

from django.shortcuts import render
from django.conf import settings as conf_settings


# Create your views here.

def indexpage(request):
    context = {
        'page_title': 'главная'
        }
    return render(request, 'mainapp/index.html', context=context)  # в пространстве имен mainapp


def products(request):
    context = {
        'page_title': 'каталог'
        }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    with open(os.path.join(conf_settings.STATICFILES_DIRS[0], 'data', 'saveddata.json'), 'r') as f:
        locations = json.load(f)
    context = {
        'page_title': 'контакты',
        'locations': locations,
        }
    return render(request, 'mainapp/contact.html', context=context)
