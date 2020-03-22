from django.db import models

from ecommerce.product.models import Book, EBook
from ecommerce.shipping.models import Ground, Air, Sea
from ecommerce.user.models.user_profile import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True, db_column='product_book')
    e_book = models.ForeignKey(EBook, on_delete=models.CASCADE, blank=True, null=True, db_column='product_e_book')

    ground = models.ForeignKey(Ground, on_delete=models.CASCADE, blank=True, null=True, db_column='shipping_ground')
    air = models.ForeignKey(Air, on_delete=models.CASCADE, blank=True, null=True, db_column='shipping_air')
    sea = models.ForeignKey(Sea, on_delete=models.CASCADE, blank=True, null=True, db_column='shipping_sea')
