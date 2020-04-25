from django.db import models

from ecommerce.order.models import Order
from ecommerce.shipping.models import Shipping


class Sea(Shipping):
    order = models.ForeignKey(Order, related_name='sea', on_delete=models.CASCADE)

    @property
    def value(self):
        return self.cost * self.weight


class Ground(Shipping):
    order = models.ForeignKey(Order, related_name='ground', on_delete=models.CASCADE)

    @property
    def value(self):
        return self.cost * self.weight


class Air(Shipping):
    order = models.ForeignKey(Order, related_name='air', on_delete=models.CASCADE)

    @property
    def value(self):
        return self.cost * self.weight

