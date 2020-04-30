from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from ecommerce.user.models import UserProfile
from ecommerce.user.serializers.user_serializer import UserProfileSerializer


class UserProfileModelViewSet(ModelViewSet):

    authentication_classes = [SessionAuthentication]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
