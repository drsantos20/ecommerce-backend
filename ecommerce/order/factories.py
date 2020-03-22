import factory

from ecommerce.order.models.order import Order, OrderDetail
from ecommerce.product.factories import BookFactory, EBookFactory
from ecommerce.shipping.factories import SeaFactory, AirFactory, GroundFactory
from ecommerce.user.factories import UserFactory


class OrderFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order


class OrderDetailFactory(factory.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    book = factory.SubFactory(BookFactory)
    e_book = factory.SubFactory(EBookFactory)

    sea = factory.SubFactory(SeaFactory)
    ground = factory.SubFactory(GroundFactory)
    air = factory.SubFactory(AirFactory)

    class Meta:
        model = OrderDetail
