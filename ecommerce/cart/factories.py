import factory

from ecommerce.cart.models import CartItem
from ecommerce.cart.models.cart import Cart
from ecommerce.product.factories import ProductVariationFactory
from ecommerce.user.factories import UserProfileFactory


class CartFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserProfileFactory)

    @factory.post_generation
    def items(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                obj.items.add(product)

    class Meta:
        model = Cart


class CartItemFactory(factory.DjangoModelFactory):
    cart = factory.SubFactory(CartFactory)
    item = factory.LazyAttribute(ProductVariationFactory)
    quantity = factory.Faker('pyint')

    @factory.post_generation
    def item(obj, create, extracted, **kwargs):
        if not create:
            return

    class Meta:
        model = CartItem
