#!/usr/bin/python3
""" Check if an object is an instance of a class
    or inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
        Return:
            bool: True if an instance or false
    """
    return isinstance(obj, a_class)
