#!/usr/bin/python3
"""
creating a private instance attribute
"""


class Square:
    """
    class square

    Attributes:
        __size: a private instance attribute
    """

    def __init__(self, size):
        self.__size = size
