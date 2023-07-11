#!/usr/bin/python3
""" A function that creates an Object from a “JSON file """


def load_from_json_file(filename):
    """ file to read from """
    import json
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
        return data
