from django.test import TestCase

from ecommerce.order.factories import OrderFactory
from ecommerce.order.models.order import Order
from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.shipping.factories import SeaFactory
from ecommerce.user.factories import UserFactory


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.order = OrderFactory(user=self.user)
        self.book = BookFactory(weight=10, price=2, order=self.order)
        self.sea = SeaFactory(cost=10, weight=self.book.weight, order=self.order)

        self.user_with_e_book_order = UserFactory()
        self.order_with_e_book = OrderFactory(user=self.user)
        self.e_book = EBookFactory(price=1, order=self.order_with_e_book)

    def test_get_order(self):
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.user, self.user)

    def test_get_order_detail_with_book(self):
        order = Order.objects.get(id=self.order.id)
        books = order.books.first()

        self.assertEqual(order.id, self.order.id)
        self.assertEqual(books.id, self.book.id)

    def test_get_order_with_e_book(self):
        order = Order.objects.get(id=self.order_with_e_book.id)
        e_books = order.ebooks.first()

        self.assertEqual(e_books.id, self.e_book.id)
