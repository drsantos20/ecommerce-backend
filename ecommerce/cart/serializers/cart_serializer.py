from rest_framework import serializers

from ecommerce.cart.models import Cart
from ecommerce.product.models import Product
from ecommerce.user.models import UserProfile
from ecommerce.user.serializers.user_serializer import generic_serializer


class CartSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    @property
    def request_user(self):
        user = None
        if 'request' in self.context:
            user = self.context.get('request')
        return user

    def get_user(self, instance):
        user_profile_serializer = generic_serializer(UserProfile)
        return user_profile_serializer(self.request_user).data

    def get_items(self, instance):
        product_serializer = Product.get_serializer()
        serializer = product_serializer(self.context.get('items'), many=True)
        return serializer

    class Meta:
        model = Cart

