"""
Создаем два файла json с данными для последующей загрузки в таблицы
ProductCategory
Product
"""

import json

CATEGORY_FILE = "_categ.json"
PRODUCT_FILE = "_prod.json"

CATEGORY_DATA = [
    {
        "name": "дом",
        "description": "продукты для дома",
        "short_descr": "короткое описание продуктов для дома",
    },
    {
        "name": "офис",
        "description": "продукты для офиса",
        "short_descr": "короткое описание продуктов для офиса",
    },
    {
        "name": "классика",
        "description": "описание классических продуктов",
        "short_descr": "короткое описание классики",
    },
    {
        "name": "модерн",
        "description": "описание модерновых товаров",
        "short_descr": "коротко о модерне",
    },
]

PRODUCT_DATA = [
    {
        "name": "Стул №1",
        "image": "product_images/product-1.jpg",
        "description": "Стул №1",
        "short_desc": "коротко о Стул №1",
        "price": 10,
        "quantity": 0,
        "category": "дом",
    },
    {
        "name": "Стул №2",
        "image": "product_images/product-2.jpg",
        "description": "Стул №2",
        "short_desc": "коротко о Стул №2",
        "price": 20,
        "quantity": 0,
        "category": "дом",
    },
    {
        "name": "Стул №3",
        "image": "product_images/product-3.jpg",
        "description": "Стул №3",
        "short_desc": "коротко о Стул №3",
        "price": 30,
        "quantity": 0,
        "category": "дом",
    },
    {
        "name": "Стул №4",
        "image": "product_images/product-4.jpg",
        "description": "Стул №4",
        "short_desc": "коротко о Стул №4",
        "price": 40.40,
        "quantity": 0,
        "category": "дом",
    },
    {
        "name": "Стул №5",
        "image": "product_images/product-5.jpg",
        "description": "Стул №5",
        "short_desc": "коротко о Стул №5",
        "price": 50.50,
        "quantity": 0,
        "category": "офис",
    },
    {
        "name": "Стул №6",
        "image": "product_images/product-11.jpg",
        "description": "Стул №16",
        "short_desc": "коротко о Стул №6",
        "price": 60,
        "quantity": 0,
        "category": "офис",
    },
    {
        "name": "Стул №7",
        "image": "product_images/product-21.jpg",
        "description": "Стул №7",
        "short_desc": "коротко о Стул №7",
        "price": 70.70,
        "quantity": 0,
        "category": "офис",
    },
    {
        "name": "Стул №9",
        "image": "product_images/product-31.jpg",
        "description": "Стул №9",
        "short_desc": "коротко о Стул №9",
        "price": 90.90,
        "quantity": 0,
        "category": "классика",
    },
    {
        "name": "Стул №10",
        "image": "product_images/product-41.jpg",
        "description": "Стул №10",
        "short_desc": "коротко о Стул №10",
        "price": 100.10,
        "quantity": 0,
        "category": "классика",
    },
    {
        "name": "Стул №11",
        "image": "product_images/product-51.jpg",
        "description": "Стул №11",
        "short_desc": "коротко о Стул №11",
        "price": 110.10,
        "quantity": 0,
        "category": "модерн",
    },
    {
        "name": "Стул №12",
        "image": "product_images/product-61.jpg",
        "description": "Стул №12",
        "short_desc": "коротко о Стул №12",
        "price": 120.20,
        "quantity": 0,
        "category": "модерн",
    },
]

if __name__ == "__main__":
    with open(CATEGORY_FILE, "w") as f:
        json.dump(CATEGORY_DATA, f)

    with open(PRODUCT_FILE, "w") as f:
        json.dump(PRODUCT_DATA, f)
