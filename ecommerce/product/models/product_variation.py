from django.db import models

from ecommerce.product.models import Product


class ProductVariation(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True)
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, related_name='product_variation_set', on_delete=models.CASCADE)

    @property
    def get_price(self):
        return self.sale_price if self.sale_price else self.price
