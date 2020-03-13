import factory

from ecommerce.shipping.models import Sea, Air, Ground, Shipping


class ShippingFactory(factory.DjangoModelFactory):
    cost = factory.Iterator([1, 2])
    shipment_type = factory.Iterator([1, 2, 3])
    name = factory.Faker('pystr')

    class Meta:
        model = Shipping
        abstract = True


class SeaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Sea


class GroundFactory(factory.DjangoModelFactory):
    class Meta:
        model = Ground


class AirFactory(factory.DjangoModelFactory):
    class Meta:
        model = Air
