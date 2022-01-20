"""debisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
import mainapp.views as mainapp

app_name = "mainapp"  # обозначили имя приложения для указанного NS

urlpatterns = [
    re_path(r"^$", mainapp.indexpage, name="index"),
    # path('products/', mainapp.products, name='products'),          # вместо path применяем re_path
    re_path(r"^products/", mainapp.products, name="products"),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    # path('category/<int:pk>/', mainapp.category, name='category'),
    re_path(r"^category/(?P<pk>\d+)/", mainapp.category, name="category"),
]
