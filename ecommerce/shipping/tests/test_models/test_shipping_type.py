
from django.test import TestCase

from ecommerce.order.constants import SEA, AIR, GROUND
from ecommerce.shipping.factories import Shipping, ShippingFactory


class ShippingTypeTestCase(TestCase):
    def setUp(self):
        self.sea = ShippingFactory(weight=10, cost=2, shipment_type=SEA)
        self.ground = ShippingFactory(weight=10, cost=1, shipment_type=GROUND)
        self.air = ShippingFactory(weight=10, cost=4, shipment_type=AIR)

    def test_get_sea_cost(self):
        sea = Shipping.objects.get(id=self.sea.id)
        self.assertEqual(sea.value, 20)

    def test_get_ground_cost(self):
        ground = Shipping.objects.get(id=self.ground.id)
        self.assertEqual(ground.value, 10)

    def test_get_air_cost(self):
        air = Shipping.objects.get(id=self.air.id)
        self.assertEqual(air.value, 40)
