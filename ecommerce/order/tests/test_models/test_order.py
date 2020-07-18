from django.test import TestCase

from ecommerce.order.factories import OrderFactory
from ecommerce.order.models.order import Order
from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.user.factories import UserFactory


class OrderTestCase(TestCase):
    def setUp(self):
        pass
