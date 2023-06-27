#!/usr/bin/python3
"""
     class Square that defines a square.
     Private instance attribute: siz
     Public instance method:
     def area(self): that returns the current square area
"""


class Square:
    """
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

    def area(self):
        d = self.__size
        return (d * d)
