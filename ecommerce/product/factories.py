import factory

from ecommerce.product.models import (
    Product,
    Book,
    EBook,
    Category,
)
from ecommerce.product.models.product_variation import ProductVariation


class CategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.DjangoModelFactory):
    price = factory.Faker('pyint')
    categories = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def categories(obj, create, extracted, **kwargs):
        if not create:
            return

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


class ProductVariationFactory(factory.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)
    title = factory.Faker('pystr')
    price = factory.Faker('pyint')
    sale_price = factory.Faker('pyint')
    inventory = factory.Faker('pyint')

    class Meta:
        model = ProductVariation

