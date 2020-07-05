from django.db import models

from ecommerce.cart.models.cart import Cart
from ecommerce.product.models.variation import Variation


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return self.item.title

    @property
    def item_name(self):
        return self.item.get_title()

    def remove(self):
        return self.item.remove_from_cart()

    @property
    def item_total(self):
        return self.item.get_price() * self.quantity