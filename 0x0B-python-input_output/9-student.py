#!/usr/bin/python3
""" A class student """


class Student:
    """
         Attribute:
            first_name(str): first name of student instance
            last_name(str): last name of student
            age(int): student age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if isinstance(self, object):
            description = {}
            for attr in self.__dict__:
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    description[attr] = value
        return description
