#!/usr/bin/python3
""" This function writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ Args:
            my_obj: object to convert to json
            filename: file to write JSON rep of python obj
    """
    import json
    with open(filename, "w", encoding="utf-8")as f:
        json.dump(my_obj, f)
