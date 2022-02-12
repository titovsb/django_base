# from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models

# Create your models here.
from mainapp.models import Product


class CartItem(models.Model):
    # related_name для views доступа
    # user = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="cart"
    # )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtty = models.PositiveIntegerField("кол-во", default=0)
    add_datetime = models.DateTimeField("время", auto_now_add=True)
    update_time = models.DateTimeField("обновлено", auto_now=True)

    @property
    def product_cost(self):
        "получаем цену товаров на одной строке"
        return self.product.price * self.qtty
    # product_cost = property(_get_product_cost)

    @property
    def total_quantity(self):
        "получаем количество товаров всего заказа пользователя"
        _items = CartItem.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.qtty, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        "получить цену всего заказа пользователя"
        _items = CartItem.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

