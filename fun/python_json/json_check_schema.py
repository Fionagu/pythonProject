# > pip install jsonschema
from jsonschema import validate
import json


schema = {
    "type": "object",
    "properties":{
        "price": {"type":"number"},
        "name":{"type":"string"},
    },
}

v = validate(instance={"name":"Eggs","price":34.99},schema = schema)

validate(instance={"name":"Eggs","price":"invalida"},schema = schema)
