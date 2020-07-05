import factory

from ecommerce.cart.factories import CartFactory
from ecommerce.order.models.order import Order
from ecommerce.shipping.factories import ShippingFactory
from ecommerce.user.factories import UserFactory


class OrderFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    cart = factory.SubFactory(CartFactory)
    shipping = factory.SubFactory(ShippingFactory)

    class Meta:
        model = Order
