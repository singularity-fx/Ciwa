from ProductData import product_data, synonyms, products, product_options, color_options, size_options, colors, sizes


def make_response_for_search(chatRequest, training={}):
    tokens = chatRequest["userInput"]["inputText"].split(" ")
    product = identify_product(tokens)
    if product:
        chatRequest["response"]["search"] = chatRequest["response"]["search"] + [product]
        items = find_product(product)
        options = {}
        for i in range(5):
            options[str(i)] = items[i]
        chatRequest["response"]["responseText"] = "Tap on the options below to shop. or say more for more options"
        chatRequest["response"]["options"] = options
        chatRequest["training"] = training if training != {} else chatRequest.get("training", {})

    else:
        if chatRequest.get("response", {}).get("search"):
            chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["product"]
        else:
            chatRequest["response"]["search"] = ["product"]
        chatRequest["response"]["responseText"] = "Great, What are you shopping today?"
        chatRequest["response"]["options"] = product_options
        chatRequest["training"] = training if training != {} else chatRequest.get("training", {})
    return chatRequest


def make_response_for_product(chatRequest, training={}):
    print("============make_response_for_product============")
    _searchPath = chatRequest.get("response").get("search")
    if _searchPath and chatRequest["userInput"]["selectedOptions"]:
        for k in chatRequest["response"]["options"].keys():
            if chatRequest["userInput"]["selectedOptions"][0] != k:
                chatRequest["response"]["options"].pop(k)
            else:
                selectedOption_key = chatRequest["response"]["options"][k]["key"]
                print(chatRequest["response"]["search"], selectedOption_key)
                chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["shirts"]
                print(chatRequest["response"]["search"])
                items = find_product(selectedOption_key)
                options = {}
                if items:
                    for i in range(5):
                        _item = items[i]
                        _item["redirectUrl"] = None
                        options[str(i)] = _item
                else:
                    break
                options["5"] = {
                    "key": "show-more",
                    "h1Text": "Show more",
                    "h2Text": None,
                    "image": "",
                    "redirectUrl": "https://www.lifestylestores.com/in/en/"
                }
                chatRequest["response"][
                    "responseText"] = "Tap on the options below to shop"
                chatRequest["response"]["options"] = options
                chatRequest["training"] = training if training != {} else chatRequest.get("training", {})
                return chatRequest
        print(_searchPath)

        if _searchPath[_searchPath.__len__() - 1] in ["shirts", "shoes", "tshirt"]:
            chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["color"]
            chatRequest["response"]["responseText"] = "Nice Choice! what color do u like?"
            chatRequest["response"]["options"] = chatRequest["response"]["options"][chatRequest["userInput"]["selectedOptions"][0]]["colors"]
        elif _searchPath[_searchPath.__len__() - 1] in ["color"]:
            chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["size"]
            chatRequest["response"]["responseText"] = "that my favorite color, select you size?"
            chatRequest["response"]["options"] = size_options
        elif _searchPath[_searchPath.__len__() - 1] == "size":
            chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["done"]
            chatRequest["response"]["responseText"] = "click on the link below to checkout"
            chatRequest["response"]["options"] = {
                "0": {
                    "key": "show-more",
                    "h1Text": "Show more",
                    "h2Text": None,
                    "image": "",
                    "redirectUrl": "https://www.lifestylestores.com/in/en/"
                }
            }

        return chatRequest
    else:
        tokens = chatRequest["userInput"]["inputText"].split(" ")
        # check for Home response
        if tokens.__len__() < 3:
            for _t in tokens:
                print(_t)

                if standardize(_t) in ["shirts", "shoes", "tshirt"]:
                    items = find_product(_t)
                    options = {}
                    if items:
                        for i in range(5):
                            _item = items[i]
                            _item["redirectUrl"] = None
                            options[str(i)] = _item
                    else:
                        break
                    options["5"] = {
                        "key": "show-more",
                        "h1Text": "Show more",
                        "h2Text": None,
                        "image": "",
                        "redirectUrl": "https://www.lifestylestores.com/in/en/"
                    }
                    chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["shirts"]
                    chatRequest["response"]["responseText"] = "Great, tap on the item to shop?"
                    chatRequest["response"]["options"] = options
                    return chatRequest
                elif _t.lower() in colors:
                    print(_t.lower() in colors)
                    chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["color"]
                    chatRequest["response"]["responseText"] = "Nice Choice! what color do u like?"
                    chatRequest["response"]["options"] = size_options
                    return chatRequest
                elif _t in sizes:
                    chatRequest["response"]["search"] = chatRequest["response"]["search"] + ["size"]
                    chatRequest["response"]["responseText"] = "click on the link below to checkout"
                    chatRequest["response"]["options"] = {
                        "0": {
                            "key": "show-more",
                            "h1Text": "Show more",
                            "h2Text": None,
                            "image": "",
                            "redirectUrl": "https://www.lifestylestores.com/in/en/"
                        }
                    }
                    return chatRequest


def find_product(product, product_type=None):
    items = []
    if product and product_type:
        product = standardize(product)
        product_type = standardize(product_type)
        items = product_data.get(product).get(product_type).get("items")
    elif product:
        product = standardize(product)
        print("product: {}".format(product))
        products = product_data.get(product)
        if products:
            for key in products.keys():
                items = items + products[key].get('items')
        print(items)
    return items


def standardize(name):
    for _t in synonyms.keys():
        for _i in synonyms[_t]:
            if _i == name.lower():
                return _t


def identify_product(tokens):
    for _i in tokens:
        _i = standardize(_i)
        if _i in products:
            return _i

