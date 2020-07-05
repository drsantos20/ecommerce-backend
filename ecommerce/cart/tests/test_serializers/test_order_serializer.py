from django.test import TestCase

from ecommerce.order.factories import OrderFactory
from ecommerce.order.serializers.order_serializer import OrderSerializer


class TestOrderSerializer(TestCase):

    def setUp(self) -> None:
        self.order = OrderFactory()
        self.order_serializer = OrderSerializer(self.order)

    def test_get_order_serializer(self):
        import pdb; pdb.set_trace()
        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data['id'], self.order.id)
