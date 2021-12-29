from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from mainapp.models import Product


class CartItem(models.Model):
    # related_name для views доступа
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtty = models.PositiveIntegerField('кол-во', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)
    update_time = models.DateTimeField('обновлено', auto_now=True)
