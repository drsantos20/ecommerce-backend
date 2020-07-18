from unittest import TestCase

from ecommerce.product.factories import ProductFactory
from ecommerce.product.models import Product, Variation


class TestProductVariationCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory()

    def test_get_product_variation(self):
        product = Product.objects.get(id=self.product.id)
        variation = Variation.objects.get(product__id=product.id)
        self.assertEqual(self.product.id, product.id)
        self.assertTrue(variation.active)
