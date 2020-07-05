from django.db import models

from ecommerce.product.models.product import Product


class Book(Product):
    weight = models.PositiveIntegerField(help_text='in grams')


class EBook(Product):
    download_link = models.URLField()
