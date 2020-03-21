import factory

from ecommerce.product.models import (
    Product,
    Book,
    EBook,
)


class ProductFactory(factory.DjangoModelFactory):
    price = factory.Iterator([1, 2])
    name = factory.Faker('pystr')

    class Meta:
        model = Product
        abstract = True


class BookFactory(factory.DjangoModelFactory):
    weight = factory.Iterator([1, 2])

    class Meta:
        model = Book


class EBookFactory(factory.DjangoModelFactory):
    download_link = factory.Faker('pystr')

    class Meta:
        model = EBook
