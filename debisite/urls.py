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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import include
# from django.urls import re_path

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.indexpage, name="main"),
    path("products/", include("mainapp.urls", namespace="primary")),
    path("contact/", mainapp.contact, name="contact"),
    path("signin/", include("authapp.urls", namespace="auth")),
    path("cart/", include("cartapp.urls", namespace="cart")),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
    path("standartadmin/", admin.site.urls),
    path("console/", include("adminapp.urls", namespace="console")),
    path("", include("social_django.urls", namespace="social")),
]
# urlpatterns = [
#     re_path(r"^$", mainapp.indexpage, name="main"),
#     re_path(r"^products/", include("mainapp.urls", namespace="primary")),
#     re_path(r"^contact/", mainapp.contact, name="contact"),
#     re_path(r"^signin/", include("authapp.urls", namespace="auth")),
#     re_path(r"^cart/", include("cartapp.urls", namespace="cart")),
#     re_path(r"^order/", include("ordersapp.urls", namespace="order")),
#     re_path(r"^standartadmin/", admin.site.urls),
#     re_path(r"^console/", include("adminapp.urls", namespace="console")),
#     re_path(r"^$", include("social_django.urls", namespace="social")),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
