import graphene
from graphene_django import DjangoObjectType

from ecommerce.user.models import UserProfile


class UserQueryType(DjangoObjectType):
    class Meta:
        model = UserProfile


class Query(object):
    all_users = graphene.List(UserQueryType)

    def resolve_all_users(self, info, **kwargs):
        return UserProfile.objects.all()
