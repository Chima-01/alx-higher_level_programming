#!/usr/bin/python3
""" Creates a class square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Attributes:
            size: size of square
            x: x-coordinate
            y: y-coordinate
            id: identifier
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height of square instance"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update square class"""
        order = ["id", "size", "x", "y"]

        if args is not None and len(args) != 0:
            for a in range(len(args)):
                setattr(self, order[a], args[a])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
       """returns square in dict type"""
       return {"id": self.id, "x": self.x, "size": self.size,
               "y": self.y}
