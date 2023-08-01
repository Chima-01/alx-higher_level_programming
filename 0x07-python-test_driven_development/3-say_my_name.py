#!/usr/bin/python3
"""
    A function that prints My name is
    <first name> <last name>
    raises error if name not str
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if len(first_name) != 0 and len(last_name) == 0:
         return print("My name is {:s}".format(first_name))

    return print("My name is {:s} {:s}".format(last_name, last_name))
