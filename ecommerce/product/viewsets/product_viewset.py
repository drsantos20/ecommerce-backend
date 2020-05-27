from rest_framework import viewsets

from ecommerce.product.serializers.product_serializer import ProductGenericSerializer


class GeneralViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.kwargs.get('model')
        return model.objects.all()

    def get_serializer_class(self):
        ProductGenericSerializer.Meta.model = self.kwargs.get('model')
        return ProductGenericSerializer
