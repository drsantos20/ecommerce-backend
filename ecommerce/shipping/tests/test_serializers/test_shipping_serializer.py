from django.test import TestCase

from ecommerce.shipping.factories import ShippingFactory
from ecommerce.shipping.serializers.shipping_serializer import ShippingSerializer


class TestShippingSerializer(TestCase):
    def setUp(self) -> None:
        self.shipping = ShippingFactory()
        self.shipping_serializer = ShippingSerializer(self.shipping)

    def test_get_shipping_serializer(self):
        serializer_data = self.shipping_serializer.data
        self.assertEqual(serializer_data['name'], self.shipping.name)
        self.assertEqual(serializer_data['weight'], self.shipping.weight)
        self.assertEqual(serializer_data['shipment_type'], self.shipping.shipment_type)
