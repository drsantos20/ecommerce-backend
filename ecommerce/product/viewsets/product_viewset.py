from rest_framework.viewsets import ModelViewSet

from ecommerce.product.utils import get_model_by_name, url_params_validation


class ProductViewSet(ModelViewSet):

    def get_queryset(self):
        model_name = url_params_validation(self.kwargs)
        product = get_model_by_name(model_name)
        return product.objects.all()

    def get_serializer_class(self):
        model_name = url_params_validation(self.kwargs)
        product = get_model_by_name(model_name)
        serializer_class = product.get_serializer()
        return serializer_class
