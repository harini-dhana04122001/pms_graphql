from flask import Blueprint, request, Response
from pms_app.building.model import Building

# from pms_app.building.service import create_building_details

display = Blueprint('display', __name__)


# @display.route('/', methods=['POST'])
# def create_detail():
#     book_data = request.get_json()
#     name = book_data['name']
#     agent_name = book_data['agent_name']
#     agent_contact = book_data['agent_contact']
#     create_building_details(name, agent_name, agent_contact)
#     return Response('successfully created')

