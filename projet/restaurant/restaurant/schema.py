import graphene
import resto.schema


class Query(resto.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)