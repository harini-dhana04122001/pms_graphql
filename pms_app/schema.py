import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from pms_app.community.model import Community
# from pms_app.community.service import create_community_details


class CommunityObject(SQLAlchemyObjectType):
    class Meta:
        model = Community
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_community = SQLAlchemyConnectionField(CommunityObject)


# class AddCommunity(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#         agent_name = graphene.String(required=True)
#         agent_contact = graphene.String(required=True)
#     community = graphene.Field(lambda: CommunityObject)
#
#     def mutate(self, info, name, agent_name, agent_contact):
#         community = Community(name, agent_name, agent_contact)
#         create_community_details(community)
#         return AddCommunity(community=community)
#
#
# class Mutation(graphene.ObjectType):
#     add_community = AddCommunity.Field()


# community_schema = graphene.Schema(query=Query, mutation=Mutation)
community_schema = graphene.Schema(query=Query)
