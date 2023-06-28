#!/usr/bin/python3
""" defines a square """


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

    def my_print(self):
        """ print char # in stdout """
        if self.size == 0:
            print()
        for x in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
