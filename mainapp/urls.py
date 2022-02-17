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
from django.urls import path
import mainapp.views as mainapp

app_name = "mainapp"  # обозначили имя приложения для указанного NS

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("category/<int:pk>/", mainapp.category, name="category"),
    path("category/<int:pk>/page/<int:page>/", mainapp.category, name="page"),
    path("product/<int:pk>/<slug:slug>/", mainapp.product, name="product")
]
# urlpatterns = [
#     re_path(r"^$", mainapp.products, name="index"),
#     re_path(r"^category/(?P<pk>\d+)/$", mainapp.category, name="category"),
#     re_path(r"category/(?P<pk>\d+)/page/(?P<page>\d+)/$", mainapp.category, name="page"),
#     re_path(r"product/(?P<pk>\d+)/(?P<slug>.+)/$", mainapp.product, name="product")
# ]
