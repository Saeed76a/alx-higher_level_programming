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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """
    define width
    """
    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value (int): the value of width
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """
    define height
    """
    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value (int): the value of height
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """
    define x
    """
    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        Args:
            value (int): the value of x
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """
    define y
    """
    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        Args:
            value (int): the value of y
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
