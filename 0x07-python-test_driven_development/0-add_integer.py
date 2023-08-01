#!/usr/bin/python3
""" 
    This function adds only integers or floats
    Raises an error if not int or float
    a and b are casted to integers if they are float
"""


def add_integer(a, b=98):
    """
        adds a and b if they of type float or int
    """

    check = [float, int]

    if type(a) not in check:
        raise TypeError('a must be an integer')
    if type(b) not in check:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
