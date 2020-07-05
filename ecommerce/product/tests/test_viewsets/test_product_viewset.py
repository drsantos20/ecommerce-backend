import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.order.factories import OrderFactory
from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.product.models import EBook, Book


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.book = BookFactory()
        self.e_book = EBookFactory()

    def test_get_all_books(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1', 'type': 'book'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        book_data = json.loads(response.content)[0]

        self.assertEqual(book_data['weight'], self.book.weight)

    def test_get_all_e_books(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1', 'type': 'ebook'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        e_book_data = json.loads(response.content)[0]

        self.assertEqual(e_book_data['download_link'], self.e_book.download_link)

    def test_create_new_product_e_book_(self):
        pass

    def test_create_new_product_book_(self):
        pass
