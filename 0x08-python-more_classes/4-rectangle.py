#!/usr/bin/python3
"""
    Creating a private instance in class rectangle
    create a method to the area and perimter passed to
    the class
"""


class Rectangle:
    """
        Attribute:
            width(int): width of rectangle
            height(int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ find the area of the object in class rectangle """
        leng = self.__height
        b = self.__width
        return (leng * b)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        tLeng = self.__height * 2
        b = self.__width * 2

        return (tLeng + b)

    def __str__(self):
        b = ""

        if self.width == 0 or self.height == 0:
            return b

        for i in range(self.height):
            b += '#' * self.width
            if i != self.height - 1:
                b += '\n'

        return b

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
