#!/usr/bin/python3
import json
"""  a function that returns the JSON
    representation of an object (string)
"""


def to_json_string(my_obj):
    """ converts python obj to javaScript"""
    x = json.dumps(my_obj)
    return x
