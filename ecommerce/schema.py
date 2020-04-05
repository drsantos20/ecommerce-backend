import graphene

import ecommerce.user.schemas.graphql


class Query(ecommerce.user.schemas.graphql.UserQuery, graphene.ObjectType):
    pass


class Mutation(ecommerce.user.schemas.graphql.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
