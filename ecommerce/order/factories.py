import factory

from ecommerce.order.models.order import Order
from ecommerce.user.factories import UserFactory


class OrderFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order
