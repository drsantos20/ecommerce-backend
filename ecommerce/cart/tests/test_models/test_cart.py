import unittest

from ecommerce.cart.factories import CartFactory
from ecommerce.cart.models import Cart


class CartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = CartFactory()

    def test_get_cart(self):
        cart = Cart.objects.get(id=self.cart.id)
        self.assertEqual(cart.user.id, self.cart.user.id)
