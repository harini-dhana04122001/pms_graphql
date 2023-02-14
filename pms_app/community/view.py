from flask import Blueprint, request, Response
from flask_graphql import GraphQLView

from pms_app.community.model import Community
from pms_app.schema import community_schema
from pms_app.community.service import create_community_details

display = Blueprint('display', __name__)

display.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=community_schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@display.route('/', methods=['POST'])
def create_detail():
    book_data = request.get_json()
    name = book_data['name']
    agent_name = book_data['agent_name']
    agent_contact = book_data['agent_contact']
    community = Community(name,agent_name,agent_contact)
    create_community_details(community)
    return Response('successfully created')

