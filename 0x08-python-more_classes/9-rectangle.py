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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        c = self.print_symbol

        if self.width == 0 or self.height == 0:
            return b

        for i in range(self.height):
            b += str(c) * self.width
            if i != self.height - 1:
                b += '\n'

        return b

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ print this when an object is deleted """
        print("Bye rectangle...")

        """ subtract 1 from it when an obj is deleted"""
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 == area2:
            return rect_1
        elif area1 < area2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        sq = Rectangle()
        sq.width = size
        sq.height = size
        return sq
