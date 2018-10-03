from __future__ import unicode_literals
from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "more"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))





