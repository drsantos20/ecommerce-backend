from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ecommerce.product.utils import (
    get_model_by_name,
    url_params_validation,
    get_generic_serializer,
)


class ProductViewSet(ModelViewSet, CreateModelMixin):

    def get_queryset(self):
        model_name = url_params_validation(self.kwargs)
        product = get_model_by_name(model_name)
        return product.objects.all()

    def create(self, request, *args, **kwargs):
        serializer_from_model = get_generic_serializer(self.kwargs)
        serializer = serializer_from_model(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_class(self):
        serializer_class = get_generic_serializer(self.kwargs)
        return serializer_class
