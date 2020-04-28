
from django.test import TestCase

from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.product.models import Book, EBook
from ecommerce.shipping.factories import SeaFactory
from ecommerce.shipping.models import Sea


class BookTestCase(TestCase):
    def setUp(self):
        self.book = BookFactory(weight=10, price=2)
        self.e_book = EBookFactory(download_link='http://drsantos20.com.br/batman', price=1)

    def test_get_book(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.price, 2)
        self.assertEqual(book.weight, 10)

    def test_get_ebook(self):
        e_book = EBook.objects.get(id=self.book.id)
        self.assertEqual(e_book.price, 1)
        self.assertEqual(e_book.download_link, 'http://drsantos20.com.br/batman')
