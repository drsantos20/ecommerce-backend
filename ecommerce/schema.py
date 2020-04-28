import graphene
from django.contrib.auth.models import User
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
        username = kwargs.get('username')

        if id is not None:
            return UserProfile.objects.get(pk=id)

        if email is not None:
            return UserProfile.objects.get(email=email)

        if username is not None:
            return User.objects.get(username=username)

        return None


class UpdateUser(graphene.Mutation):
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
        return UpdateUser(user=user)


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        username = graphene.String()

    user = graphene.Field(UserQueryType)

    def mutate(root, info, **input):
        user = User.objects.create_user(
            email=input.get('email'),
            username=input.get('username')
        )
        user_profile = UserProfile.objects.create(user=user, email=input.get('email'))

        return CreateUser(user=user_profile)


class Mutation(graphene.ObjectType):
    update_user = UpdateUser.Field()
    create_user = CreateUser.Field()
