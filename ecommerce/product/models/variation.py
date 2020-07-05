from django.db import models

from ecommerce.product.models import Product


class Variation(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True)
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def get_price(self):
        """
        return sale price if not None otherwise return prices
        """
        return self.sale_price if self.sale_price else self.price
