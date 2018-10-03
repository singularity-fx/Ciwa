from pprint import pprint

from application import app
from flask import request, jsonify

from application.controllers.DialogueFlow import getResponse


@app.route('/conversation', methods=['POST'])
def get_chat_page():
    _request = request.json
    pprint(_request)
    _response = getResponse(_request)
    return jsonify(_response)

