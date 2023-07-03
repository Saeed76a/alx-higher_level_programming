#!/usr/bin/python3
"""declare the Rectangle class"""


class Rectangle:

    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the class
        Args:
            width (int): the width of rectangle
            height (int): the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ retrieve the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """retrieve the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            [rectangle.append("#") for j in range(self.__width)]
            if i < self.__height - 1:
                rectangle.append("\n")
        recstring = "".join(rectangle)
        return recstring
