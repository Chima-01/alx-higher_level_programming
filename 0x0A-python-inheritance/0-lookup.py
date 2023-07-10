#!/usr/bin/python3

""" This function returns list of available attributes
    and methods of an object
"""


def lookup(obj):
    if obj:
        return dir(obj)
