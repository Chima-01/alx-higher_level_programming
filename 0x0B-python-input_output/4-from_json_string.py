#!/usr/bin/python3
""" This function returns an object(Python data structure)
    represented by a JSON string
"""


def from_json_string(my_str):
    """ return python obj """
    import json
    f = json.loads(my_str)
    return f
