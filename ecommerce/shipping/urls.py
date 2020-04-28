from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from ecommerce.shipping.schema import schema

urlpatterns = [
    url(r'^shipping/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

