import graphene

import ecommerce.schema


class Query(ecommerce.schema.UserQuery, graphene.ObjectType):
    pass


class Mutation(ecommerce.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
