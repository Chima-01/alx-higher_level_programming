#!/usr/bin/python3
""" Checks if anargument is a subclass """


def inherits_from(obj, a_class):
    """
    Return: True if instance else False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
