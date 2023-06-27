#!/usr/bin/python3
"""
    A square class that defines class:
    Private instance attribute: size
"""


class Square:
    """
    class square

    Attributes:
        __size: private instance attribute
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
