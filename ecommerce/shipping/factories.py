import factory

from ecommerce.order.factories import OrderFactory
from ecommerce.shipping.models import Shipping


class ShippingFactory(factory.DjangoModelFactory):
    cost = factory.Iterator([1, 2])
    shipment_type = factory.Iterator([1, 2, 3])
    name = factory.Faker('pystr')
    order = factory.SubFactory(OrderFactory)

    class Meta:
        model = Shipping
