from django.db import models

from ecommerce.order.models import Order
from ecommerce.product.models.product import Product


class Book(Product):
    weight = models.PositiveIntegerField(help_text='in grams')
    order = models.ForeignKey(Order, related_name='books', on_delete=models.CASCADE)


class EBook(Product):
    download_link = models.URLField()
    order = models.ForeignKey(Order, related_name='ebooks', on_delete=models.CASCADE)
