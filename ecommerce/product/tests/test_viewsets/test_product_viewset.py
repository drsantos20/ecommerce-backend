import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.product.factories import ProductFactory
from ecommerce.product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.product = ProductFactory()

    def test_get_all_books(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)[0]

        self.assertEqual(product_data['title'], self.product.title)
        self.assertEqual(product_data['price'], self.product.price)
        self.assertEqual(product_data['active'], self.product.active)

    def test_create_new_product_e_book(self):
        data = json.dumps({
            'title': 'samsung gear galaxy',
            'brand': 'samsung',
            'price': 800.00,
            'image': 'http://example.com/samsung_gear.png'
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title='samsung gear galaxy')

        self.assertTrue(created_product.title, 'samsung gear galaxy')
        self.assertTrue(created_product.price, 800.00)
