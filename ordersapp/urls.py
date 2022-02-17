"""debisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
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
