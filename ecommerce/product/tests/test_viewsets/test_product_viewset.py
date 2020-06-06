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
        order = OrderFactory()
        data = json.dumps({
            'name': 'harry potter kindle edition',
            'download_link': 'http://amazon.com.br/harry-potter',
            'order': order.id
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1', 'type': 'ebook'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        e_book = EBook.objects.get(name='harry potter kindle edition')
        self.assertEqual(e_book.download_link, 'http://amazon.com.br/harry-potter')

    def test_create_new_product_book_(self):
        order = OrderFactory()
        data = json.dumps({
            'name': 'harry potter',
            'weight': '500',
            'order': order.id
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1', 'type': 'book'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        book = Book.objects.get(name='harry potter')
        self.assertEqual(book.weight, 500)
