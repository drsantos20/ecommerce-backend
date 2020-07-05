from django.db import models


class Variation(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_price(self):
        """
        return sale price if not None otherwise return prices
        """
        return self.sale_price if self.sale_price else self.price
