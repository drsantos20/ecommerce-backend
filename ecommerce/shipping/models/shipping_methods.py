from django.db import models

from ecommerce.shipping.models import Shipping


class Sea(Shipping):

    @property
    def value(self):
        return self.cost * self.weight


class Ground(Shipping):

    @property
    def value(self):
        return self.cost * self.weight


class Air(Shipping):

    @property
    def value(self):
        return self.cost * self.weight

