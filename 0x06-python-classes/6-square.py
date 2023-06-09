#!/usr/bin/python3
""" defines a square """


class Square:
    """
    Atrributes:
    size:size of square
    value: property setter
    position: handle tuples
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ get/ set size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """get / set position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns area of square"""
        d = self.__size
        return d * d

    def my_print(self):

        """print char # in stdout"""
        if self.size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            print("{}".format("#") * self.size)
