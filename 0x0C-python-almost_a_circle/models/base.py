#!/usr/bin/python3
""" Creating a class called base"""
import json


class Base:
    """
        Attributes:
            id(int): instance id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dict to json str"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save a list to a file in json"""
        fi = cls.__name__ + ".json"
        content = []
        j_obj = cls.to_json_string(list_objs)

        with open(fi, "w", encoding="utf-8") as f:
            f.write(j_obj)

    @staticmethod
    def from_json_string(json_string):
        """ gets list of json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
