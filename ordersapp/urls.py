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
# from django.urls import path, re_path
from django.urls import re_path, path
import ordersapp.views as ordersapp

app_name = "ordersapp"  # обозначили имя приложения для указанного NS

urlpatterns = [
    path("", ordersapp.OrderList.as_view(), name="order_list"),
    re_path(r"^forming/(?P<pk>\d+)/$", ordersapp.slug1, name="order_forming"),
    path("create/", ordersapp.slug, name="order_create"),
    re_path(r"^read/(?P<pk>\d+)/$", ordersapp.slug1, name="order_read"),
    re_path(r"^update/(?P<pk>\d+)/$", ordersapp.slug1, name="order_update"),
    re_path(r"^delete/(?P<pk>\d+)/$", ordersapp.slug1, name="order_delete"),
]
# urlpatterns = [
#     re_path(r"^$", ordersapp.OrderList.as_view(), name="order_list"),
#     re_path(r"^forming/(?P<pk>\d+)/$", ordersapp.slug1, name="order_forming"),
#     re_path(r"^create/", ordersapp.slug, name="order_create"),
#     re_path(r"^read/(?P<pk>\d+)/$", ordersapp.slug1, name="order_read"),
#     re_path(r"^update/(?P<pk>\d+)/$", ordersapp.slug1, name="order_update"),
#     re_path(r"^delete/(?P<pk>\d+)/$", ordersapp.slug1, name="order_delete"),
# ]
