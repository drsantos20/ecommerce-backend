from django.db import models

from ecommerce.product.models import Product
from ecommerce.shipping.models import Shipping
from ecommerce.user.models.user_profile import User


class Order(models.Model):
    def __init__(self, product: Product, user: User, shipping: Shipping):
        self.product = product
        self.user = user
        self.shipping = shipping
