from django.db import models

from ecommerce.cart.models.cart_item import CartItem
from ecommerce.product.models.product_variation import ProductVariation
from ecommerce.user.models import UserProfile


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductVariation, through=CartItem)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return 'User: {} has {} items in their cart. Their total is ${}'.format(self.user, self.count, self.cart_price)

    @property
    def count(self) -> int:
        return self.cartitem_set.count()

    @property
    def cart_price(self) -> int:
        total = 0
        for item in self.cartitem_set.all():
            total += item.item_total
        return total

    @property
    def total_count(self) -> int:
        cart_count = 0
        for item in self.cartitem_set.all():
            cart_count += item.quantity
        return cart_count
