from unittest import TestCase

from ecommerce.product.factories import ProductFactory
from ecommerce.product.models import Product, ProductVariation


class TestProductVariationCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory(
            title='Nintendo Switch',
            price=299.00,
        )

    def test_get_product_variation(self):
        product = Product.objects.get(id=self.product.id)
        variation = ProductVariation.objects.get(product__id=product.id)
        self.assertEqual(self.product.id, product.id)
        self.assertTrue(variation.active)
        self.assertEqual(product.price, self.product.price)

    def test_add_discount_to_existing_product(self):
        variation = ProductVariation.objects.get(product__id=self.product.id)
        variation.sale_price = 250.00
        variation.save()

        self.assertEqual(variation.sale_price, 250)

