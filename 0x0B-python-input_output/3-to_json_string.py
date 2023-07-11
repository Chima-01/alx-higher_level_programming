#!/usr/bin/python3
"""  a function that returns the JSON
    representation of an object (string)
"""


def to_json_string(my_obj):
    """ converts python obj to javaScript """
    import json
    x = json.dumps(my_obj)
    return x
