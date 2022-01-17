import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta

from django.utils import timezone

def get_expiration_date():
    return timezone.now() + timedelta(hours=24)


# Create your models here.

class DebiUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', null=True, default=18)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    activation_key = models.CharField(verbose_name='ключ активации', max_length=64, null=True)
    expiration_date = models.DateTimeField(verbose_name='код активации истекает' ,
                                           default=get_expiration_date)

    def is_activation_expired(self):
        if timezone.now() <= self.expiration_date:
            return False
        else:
            return True
