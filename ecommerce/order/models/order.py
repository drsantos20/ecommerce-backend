from django.db import models

from ecommerce.cart.models import Cart
from ecommerce.shipping.models import Shipping
from ecommerce.user.models.user_profile import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, related_name='shipping_address', null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
