#!/usr/bin/python3
""" Creating a class called base"""
import json
import os


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
        if list_objs is None:
            list_o = []
        else:
            fi = cls.__name__ + ".json"
            list_o = [i.to_dictionary() for i in list_objs]
            j_obj = cls.to_json_string(list_o)
            with open(fi, "w", encoding="utf-8") as f:
                f.write(j_obj)

    @staticmethod
    def from_json_string(json_string):
        """ gets list of json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return instance with attribute set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Square:
            dummy = cls(1)
        elif cls is Rectangle:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as f:
            data = f.read()
            if not data or data == "[]":
                return []
            ins = []
            [ins.append(cls.create(**d)) for d in
             cls.from_json_string(data)]
            return ins
