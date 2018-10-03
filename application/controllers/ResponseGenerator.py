class ResponseGenerator:
    def __init__(self):
        pass

    @classmethod
    def make_response(cls, clientRequest, selectedTemplate, params=None, training={}):
        print("* * * * * * * * * * * * * * ")
        print("# Make Response ")
        if params:
            clientRequest["response"]["responseText"] = selectedTemplate["text"].format(
                **params)
        else:
            clientRequest["response"]["responseText"] = selectedTemplate["text"]
        if clientRequest["response"].get("search"):
            _options = get_options(clientRequest["response"]["search"])
            clientRequest["response"]["options"] = _options
        else:
            clientRequest["response"]["options"] = selectedTemplate["options"]

        clientRequest["training"] = training
        return clientRequest

    @classmethod
    def send_home_response(cls, clientRequest, home_options):
        print("* * * * * * * * * * * * * * ")
        print("# Make Home Response")
        clientRequest["response"]["responseText"] = "Do you need assistance with"
        clientRequest["response"]["options"] = home_options
        clientRequest["response"]["search"] = []
        return clientRequest


def get_options(searchPath):
    return ""
