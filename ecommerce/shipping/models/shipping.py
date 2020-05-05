from django.db import models

from ecommerce.order.constants import (
    GROUND,
    AIR,
    SEA,
)
from ecommerce.order.models import Order


class Shipping(models.Model):
    name = models.CharField(max_length=30)
    weight = models.PositiveIntegerField(null=True, default=0)
    order = models.ForeignKey(Order, related_name='shipping', on_delete=models.CASCADE)

    SHIPMENT_TYPE_CHOICES = [
        (GROUND, 'GROUND'),
        (AIR, 'AIR'),
        (SEA, 'SEA'),
    ]

    shipment_type = models.CharField(
        max_length=30,
        choices=SHIPMENT_TYPE_CHOICES,
    )

    cost = models.PositiveIntegerField(
        help_text='in cents',
        null=True,
        default=0
    )

    @property
    def value(self):
        return self.cost * self.weight

    def __str__(self) -> str:
        return self.name
