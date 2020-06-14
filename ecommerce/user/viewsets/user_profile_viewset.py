from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from ecommerce.user.utils import get_generic_serializer
from ecommerce.utils import url_params_validation, get_model_by_name


class UserProfileViewSet(ModelViewSet):

    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        model_name = url_params_validation(self.kwargs)
        user = get_model_by_name('user', model_name)
        return user.objects.all()

    def get_serializer_class(self):
        serializer_class = get_generic_serializer(self.kwargs)
        return serializer_class
