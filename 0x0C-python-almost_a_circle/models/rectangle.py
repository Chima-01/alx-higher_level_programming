#!/usr/bin/python3
""" Creating a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
        Attributes:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): x-coordinate
            y(int): y-coordinate
            id: unique identifier
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of class instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets height of class instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of class instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets instance x-coordinate value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to x-coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets instance y-coordinate value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to y-coordinate of instance"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """print triangle"""
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """ return attribues value of instance"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update class instance"""
        order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for a in range(len(args)):
                setattr(self, order[a], args[a])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ give the dictionary rep of rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
