import factory

from ecommerce.product.models import (
    Product,
    Book,
    EBook,
    Category,
)
from ecommerce.product.models.variation import Variation


class CategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')

    class Meta:
        model = Category


class ProductFactory(factory.DjangoModelFactory):
    price = factory.Faker('pyint')
    name = factory.Faker('pystr')
    categories = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product


class BookFactory(factory.DjangoModelFactory):
    weight = factory.Iterator([1, 2])

    class Meta:
        model = Book


class EBookFactory(factory.DjangoModelFactory):
    download_link = factory.Faker('pystr')

    class Meta:
        model = EBook


class VariationFactory(factory.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)
    title = factory.Faker('pystr')
    price = factory.Faker('pyint')
    sale_price = factory.Faker('pyint')
    inventory = factory.Faker('pyint')

    class Meta:
        model = Variation

