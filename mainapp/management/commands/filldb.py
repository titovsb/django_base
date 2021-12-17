import json

from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product


class Command(BaseCommand):
    help = 'Заполняем базу данных начальными значениями'

    def load_from_json(self, fn):
        with open(fn, 'r') as f:
            return json.load(f)

    def handle(self, *args, **kwargs):
        items = self.load_from_json('json/_categ.json')
        for el in items:
            ProductCategory.objects.create(**el)

        items = self.load_from_json('json/_prod.json')
        for el in items:
            category = ProductCategory.objects.get(name=el['category'])
            el['category'] = category
            Product.objects.create(**el)
