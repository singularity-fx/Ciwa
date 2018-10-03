from __future__ import unicode_literals
from pprint import pprint

from application.controllers.ProductData import home_options
from application.controllers.ProductFlow import make_response_for_search, make_response_for_product
from application.controllers.ResponseGenerator import ResponseGenerator
from application.controllers.User import User
from application.controllers.IntentClassifier import get_intent_from_model, get_intent_from_options
from application.controllers.templates import responseText


def getResponse(chatRequest):
    _response = None
    _intent = None

    tokens = chatRequest["userInput"]["inputText"].split(" ")
    # check for Home response
    if tokens.__len__() < 3:
        for _t in tokens:
            if _t in ["Home", "home", "main", "Main", "menu", "Menu"]:
                return ResponseGenerator.send_home_response(chatRequest, home_options)
            if _t.lower() in ["discounts", "discount", "offer", "offers", "off", "sale"]:
                return ResponseGenerator.make_response(chatRequest, responseText.get("discounts")[0])

    # if search path exists
    if chatRequest.get("response", {}).get("search"):
        _response = make_response_for_product(chatRequest)
        if _response:
            return _response

    # find intent
    nlu = get_intent_from_model(chatRequest["userInput"]["inputText"])
    pprint(nlu)
    if nlu["intent"].get("confidence") > 0.805:
        _intent = nlu["intent"].get("name")
    else:
        _intent = "cant-find"
    
    # find intent from options
    _intent = get_intent_from_options(chatRequest, _intent)
    
    # build response
    _response = compile_response(_intent, chatRequest, nlu)
    return _response


def compile_response(intent, chatRequest, training):
    print("-----------------------------------")
    print ("# Compiling Response ")
    _response = chatRequest
    if intent == "greet":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("greet")[0], training=training)
    elif intent == "goodbye":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("goodbye")[0], training=training)
    elif intent == "dont_like":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("dont_like")[0], training=training)
    elif intent == "show_more_items":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("show_more_items")[0],
                                                    training=training)
    elif intent == "reward-points":
        params = User.get_user_details(chatRequest["userId"])
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("reward-points")[0], params,
                                                    training=training)
    elif intent == "product":
        chatRequest["response"]["search"] = []
        _response = make_response_for_search(chatRequest, training=training)
        _response["response"]["search"] = ["product"]
    elif intent == "feedback":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("feedback")[0], training=training)
    elif intent == "discounts":
        _response = ResponseGenerator.make_response(chatRequest, responseText.get("discounts")[0], training=training)
    elif intent == "searching_for":
        print("===========1===============")
        chatRequest["response"]["search"] = []
        _response = make_response_for_search(chatRequest, training=training)
    elif intent == "cant-find":
        _response = ResponseGenerator.make_response(chatRequest, {
            "text": "Could you please rephrase",
            "options": []
        }, training=training)
    return _response

