import graphene
from graphene_django import DjangoObjectType

from ecommerce.user.models import UserProfile


class UserQueryType(DjangoObjectType):
    class Meta:
        model = UserProfile


class UserQuery(object):
    all_users = graphene.List(UserQueryType)

    user = graphene.Field(
        UserQueryType, id=graphene.Int(), name=graphene.String()
    )

    def resolve_all_users(self, info, **kwargs):
        return UserProfile.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        email = kwargs.get('email')

        if id is not None:
            return UserProfile.objects.get(pk=id)

        if email is not None:
            return UserProfile.objects.get(email=email)

        return None


class UserMutation(graphene.Mutation):
    location = graphene.String()
    email = graphene.String()

    class Arguments:
        location = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserQueryType)

    def mutate(self, info, location, email):
        user = UserProfile.objects.get(email=email)
        user.location = location
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()
