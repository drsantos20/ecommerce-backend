from django.db import models

from ecommerce.shipping.models import Shipping


class Sea(Shipping):
    weight = models.PositiveIntegerField(null=True, default=0)

    @property
    def value(self):
        return self.cost * self.weight


class Ground(Shipping):
    weight = models.PositiveIntegerField(null=True, default=0)

    @property
    def value(self):
        return self.cost * self.weight


class Air(Shipping):
    weight = models.PositiveIntegerField(null=True, default=0)

    @property
    def value(self):
        return self.cost * self.weight

