from django.test import TestCase

from ecommerce.order.factories import OrderFactory, OrderDetailFactory
from ecommerce.order.models.order import Order, OrderDetail
from ecommerce.product.factories import ProductFactory, BookFactory, EBookFactory
from ecommerce.shipping.factories import ShippingFactory, SeaFactory
from ecommerce.user.factories import UserFactory


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.book = BookFactory(weight=10, price=2)
        self.sea = SeaFactory(cost=10, weight=self.book.weight)

        self.order = OrderFactory(user=self.user)
        self.order_detail = OrderDetailFactory(book=self.book, sea=self.sea, order=self.order)

    def test_get_order(self):
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.user, self.user)

    def test_get_order_detail_with_book(self):
        order_detail = OrderDetail.objects.get(id=self.order_detail.id)
        self.assertEqual(order_detail.book, self.book)
        self.assertEqual(order_detail.order, self.order)
        self.assertEqual(order_detail.sea.value, 100)

    def test_get_order_detail_with_e_book(self):
        e_book = EBookFactory(price=1)
        order_detail = OrderDetailFactory(e_book=e_book, order=self.order)
        order_detail = OrderDetail.objects.get(id=order_detail.id)

        self.assertEqual(order_detail.e_book, e_book)
        self.assertEqual(order_detail.sea.value, 0)
