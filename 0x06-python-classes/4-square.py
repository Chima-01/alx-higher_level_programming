#!/usr/bin/python3
"""
    class Square:
        Private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method:
        def area(self): that returns the current square area
"""


class Square:
    """
        Atrributes:
        __size:size of square
        value: setter property
    """

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        d = self.__size
        return (d * d)
