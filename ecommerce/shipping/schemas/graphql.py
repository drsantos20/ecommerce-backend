import graphene
from graphene_django import DjangoObjectType

from ecommerce.shipping.models import Sea


class SeaShippingQueryType(DjangoObjectType):
    class Meta:
        model = Sea


class SeaQuery(object):
    all_sea_shipping = graphene.List(SeaShippingQueryType)

    sea = graphene.Field(
        SeaShippingQueryType, id=graphene.Int(), name=graphene.String()
    )

    def resolve_all_sea_shipping(self, info, **kwargs):
        return Sea.objects.all()

    def resolve_sea_shipping(self, info, **kwargs):
        id = kwargs.get('id')
        order_id = kwargs.get('order_id')

        if id is not None:
            return Sea.objects.get(pk=id)

        if order_id is not None:
            return Sea.objects.get(order_id=order_id)

        return None