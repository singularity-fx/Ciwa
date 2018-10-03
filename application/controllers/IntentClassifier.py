from rasa_nlu.model import Interpreter

interpreter = Interpreter.load("./models/current/nlu")


def get_intent_from_model(message):
    print("-----------------------------------")
    print ("# NLU Parsing ")
    # interpreter = Interpreter.load("../../models/current/nlu")
    result = interpreter.parse(message)
    print ("User Input Text: {}".format(message))
    print ("Intent: {name} | confidence: {confidence}".format(**result["intent"]))
    return result


def get_intent_from_options(clientRequest, nlu_intent):
    print("-----------------------------------")
    print ("# Options Parsing ")
    print ("  select Option are {}".format(clientRequest["userInput"].get("selectedOptions")))
    _intent = None
    for _selected_option in clientRequest["userInput"].get("selectedOptions"):
        if clientRequest["response"]["options"].get(_selected_option):
            print (
                "  select Option are {}".format(clientRequest["response"]["options"].get(_selected_option).get("key")))
            if clientRequest["response"]["options"].get(_selected_option).get("key") == "reward-points":
                _intent = "reward-points"
                break
            if clientRequest["response"]["options"].get(_selected_option).get("key") == "feedback":
                _intent = "feedback"
                break
            if clientRequest["response"]["options"].get(_selected_option).get("key") == "discounts":
                _intent = "discounts"
                break
            if clientRequest["response"]["options"].get(_selected_option).get("key") == "product":
                _intent = "product"
                break
    print("  intent: {}".format(_intent))
    return _intent if _intent else nlu_intent