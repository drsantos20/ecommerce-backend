import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.shipping.factories import ShippingFactory


class TestShippingViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.shipping = ShippingFactory()

    def test_get_all_shipping(self):
        response = self.client.get(
            reverse('shipping-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        shipping_data = json.loads(response.content)[0]

        self.assertEqual(shipping_data['name'], self.shipping.name)
        self.assertEqual(int(shipping_data['shipment_type']), self.shipping.shipment_type)
        self.assertEqual(shipping_data['cost'], self.shipping.cost)
