import logging

from flask import request
from flask_restplus import Resource, fields
from Ciwa.webservice.api import api
from Ciwa.webservice.serializers import conversation

log = logging.getLogger(__name__)
ns = api.namespace('ciwa', description='Ciwa Conversation APIs')


@ns.route('/api/v1/conversation')
class ConversationController(Resource):
    """Shows a list of all , and lets you POST to add new tasks"""

    @ns.doc('example text')
    @api.expect(conversation)
    @api.marshal_with(conversation)
    # @api.marshal_with(entity)
    def post(self):
        print (request)
        json_data = request.get_json(force=True)
        print(json_data)
        return json_data
