from django.urls import path, include
from rest_framework import routers

from ecommerce.user import viewsets

router = routers.SimpleRouter()
router.register(r'user/(?P<type>[-\w]+)', viewsets.UserProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
