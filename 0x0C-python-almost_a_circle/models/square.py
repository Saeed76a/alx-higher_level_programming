#!/usr/bin/python3
"""
My square
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the object with the provided arguments.

        Args:
            size (int): the size of the square
            x (int): x point of width
            y (int): y point of height
            id (int): attribute's id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """
        return
        the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter to set the size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the anstance
        """
        i = 0
        if not args:
            for attri in kwargs:
                if attri == "id":
                    self.id = kwargs[attri]
                if attri == "size":
                    self.size = kwargs[attri]
                if attri == "x":
                    self.x = kwargs[attri]
                if attri == "y":
                    self.y = kwargs[attri]

        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            i += 1

    def to_dictionary(self):
        """
        get the dictionary
        representation of a Square
        """
        return {'id': self.x, 'x': self.x, 'size\
': self.size, 'y': self.y}