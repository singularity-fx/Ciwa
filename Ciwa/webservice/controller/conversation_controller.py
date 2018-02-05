import logging

from flask import request
from flask_restplus import Resource
from Ciwa.webservice.api import api
from Ciwa.webservice.serializers import conversation

log = logging.getLogger(__name__)
ns = api.namespace('ciwa', description='Ciwa Conversation APIs')


@ns.route('/api/v1/conversation')
class ConversationController(Resource):
    """
        this is a POST api for the conversation between the user and the machine
    """

    @api.expect(conversation)
    @api.marshal_with(conversation)
    # @api.marshal_with(entity)
    def post(self):
        print(request)
        json_data = request.get_json(force=True)
        # TODO: add marshmallow serialisation and validation
        print(json_data)
        return json_data
