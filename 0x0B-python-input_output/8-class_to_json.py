#!/usr/bin/python3
""" Checks the attribute of an obj """


def class_to_json(obj):
    if isinstance(obj, object):
        description = {}

    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value

    return description
