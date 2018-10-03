intent = {
    "confidence": None,
    "name": None
}

option = {
    "key": None,
    "h1Text": None,
    "h2Text": None,
    "image": None,
    "redirectUrl": None
}

chat_request = {
    "conversationId": None,
    "sequenceNo": None,
    "userId": None,
    "userInput": {
        "inputText": None,
        "inputImage": None,
        "selectedOptions": []
    },
    "response": {
        "responseText": None,
        "options": {}
    }
}

chat_response = {
    "conversationId": None,
    "sequenceNo": None,
    "userId": None,
    "userInput": {
        "inputText": None,
        "inputImage": None,
        "selectedOptions": []
    },
    "response": {
        "responseText": None,
        "options": {}
    },
    "training": {
        "search": None,
        "entities": [],
        "intent": intent,
        "text": None,
        "intent_ranking": []
    }
}

mainOptions = {
    "0": {
        "key": "product",
        "h1Text": "Product",
        "h2Text": None,
        "image": None
    },
    "1": {
        "key": "discount",
        "h1Text": "Discount",
        "h2Text": None,
        "image": None
    },
    "2": {
        "key": "reward-points",
        "h1Text": "Reward Points",
        "h2Text": None,
        "image": None
    },
    "3": {
        "key": "feedback",
        "h1Text": "Feedback",
        "h2Text": None,
        "image": None
    }
}
