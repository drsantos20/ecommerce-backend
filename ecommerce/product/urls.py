from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from ecommerce.product import viewsets

router = routers.SimpleRouter()
router.register(r'product/(?P<type>[-\w]+)', viewsets.ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
]