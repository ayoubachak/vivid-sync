import graphene
import users.schema
import social.schema
import content.schema
import analytics.schema

class Query(
    users.schema.Query,
    social.schema.Query,
    content.schema.Query,
    analytics.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    users.schema.Mutation,
    # more classes to come
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)