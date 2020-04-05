import graphene

import ecommerce.user.schemas.graphql


class Query(ecommerce.user.schemas.graphql.UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)