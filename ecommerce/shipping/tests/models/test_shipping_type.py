
from django.test import TestCase

from ecommerce.shipping.factories import SeaFactory, GroundFactory, AirFactory
from ecommerce.shipping.models import Sea, Air, Ground


class ShippingTypeTestCase(TestCase):
    def setUp(self):
        self.sea = SeaFactory(weight=10, cost=2)
        self.ground = GroundFactory(weight=10, cost=1)
        self.air = AirFactory(weight=10, cost=4)

    def test_get_sea_cost(self):
        sea = Sea.objects.get(id=self.sea.id)
        self.assertEqual(sea.value, 20)

    def test_get_ground_cost(self):
        sea = Ground.objects.get(id=self.sea.id)
        self.assertEqual(sea.value, 10)

    def test_get_air_cost(self):
        sea = Air.objects.get(id=self.sea.id)
        self.assertEqual(sea.value, 40)
