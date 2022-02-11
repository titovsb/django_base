from django.db import models
from authapp.forms import DebiUserProfileEditForm
from authapp.models import DebiUser


# Create your models here.


class DebiUserAdminEditForm(DebiUserProfileEditForm):
    class Meta:
        model = DebiUser
        fields = "__all__"
