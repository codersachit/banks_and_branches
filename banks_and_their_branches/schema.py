import graphene

import fetch_branch_data.schema


class Query(fetch_branch_data.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)