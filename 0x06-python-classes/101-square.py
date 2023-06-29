#!/usr/bin/python3
""" creates a square """


class Square:
    """
    Attribute:
        size: get value
        area: area of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: size of square
            position: tuple
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if size == 0:
            print()

        for i in range(self.__postion[1]):
            print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            print("{}".format("#") * self.__size)

    def __str__(self):
        arr = []
        c = self.size

        if self.__size == 0:
            return ''
        if self.__position[1] >= 0 and self.__position[0] >= 0:
            for s in range(self.__position[1]):
                arr.append('\n')
        while (c):
            for b in range(self.__position[0]):
                arr.append(' ')
            for a in range(self.__size):
                arr.append('#')
            if c != 1:
                arr.append('\n')
            c -= 1
        return ''.join(arr)
