from django.urls import path, include
from rest_framework import routers

from ecommerce.shipping import viewsets

router = routers.SimpleRouter()
router.register(r'shipping', viewsets.ShippingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
