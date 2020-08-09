from unittest import TestCase

from ecommerce.product.factories import ProductFactory, CategoryFactory
from ecommerce.product.models import Product, ProductVariation


class TestProductVariationCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory()

    def test_get_product(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(self.product.id, product.id)
        self.assertEqual(self.product.price, product.price)
        self.assertEqual(self.product.description, product.description)
