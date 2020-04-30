from django.urls import path, include
from rest_framework import routers

from ecommerce.user import viewsets

router = routers.SimpleRouter()
router.register(r'users', viewsets.UserProfileModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
