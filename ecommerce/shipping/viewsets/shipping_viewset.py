from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from ecommerce.shipping.models import Shipping
from ecommerce.shipping.serializers.shipping_serializer import ShippingSerializer


class ShippingViewSet(ModelViewSet):

    authentication_classes = [SessionAuthentication]
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
