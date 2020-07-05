import factory

from ecommerce.cart.models.cart import Cart
from ecommerce.user.factories import UserFactory


class CartFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Cart
