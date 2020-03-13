
from django.test import TestCase

from ecommerce.shipping.factories import SeaFactory
from ecommerce.shipping.models import Sea


class ShippingTypeTestCase(TestCase):
    def setUp(self):
        self.sea = SeaFactory(weight=10, cost=2)

    def test_get_sea_cost(self):
        sea = Sea.objects.get(id=self.sea.id)
        self.assertEqual(sea.value, 20)
