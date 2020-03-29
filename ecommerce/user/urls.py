from django.conf.urls import url
from graphene_django.views import GraphQLView

from ecommerce.schema import schema


urlpatterns = [
    url(r'^users/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

