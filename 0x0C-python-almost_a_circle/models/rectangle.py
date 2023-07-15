#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the object with the provided arguments.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x point of width
            y (int): y point of height
            id (int): attribute's id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
