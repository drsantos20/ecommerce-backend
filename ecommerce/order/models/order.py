from django.db import models

from ecommerce.cart.models.cart import Cart
from ecommerce.shipping.models import Shipping
from ecommerce.user.models.user_profile import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, related_name='shipping_address')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
