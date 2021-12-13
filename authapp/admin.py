from django.contrib import admin

# Register your models here.
from authapp.models import DebiUser

admin.site.register(DebiUser)
