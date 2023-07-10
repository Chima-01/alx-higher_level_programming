#!/usr/bin/python3

""" This function returns list of available attributes
    and methods of an object
"""


def lookup(obj):
    """ Argument Obj an instance of a class """

    if obj:
        return dir(obj)
