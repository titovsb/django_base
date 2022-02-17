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
import cartapp.views as cartapp

app_name = "cartapp"  # обозначили имя приложения для указанного NS

urlpatterns = [
    path("", cartapp.cart, name="cart"),
    path("add/<int:pk>/", cartapp.cart_add, name="add"),
    path("remove/<int:pk>/", cartapp.cart_remove, name="remove"),
    path('edit/<int:pk>/<int:qtty>/', cartapp.cart_edit, name='edit'),
]
