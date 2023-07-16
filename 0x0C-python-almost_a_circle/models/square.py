#!/usr/bin/python3
"""
My square
"""
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
".format(self.id, super().x, super().y, super().height)
