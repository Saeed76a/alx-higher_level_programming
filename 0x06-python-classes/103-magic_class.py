#!/usr/bin/python3
"""define the Python class MagicClass that does exactly the same\
      as the following Python bytecode:"""
from math import pi


class MagicClass:
    """set a circle"""

    def __init__(self, radius):
        """intialize MagicClass:
        Args:
            radius (float and int): the raduis of the circle
        """
        self.__radius = 0
        if type(raduis) is not int and is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius
        """Return the current radius"""
        return self.__radius

    def area(self):
        """Return the area of the circle"""
        return (self.__radius ** 2 * pi)

    def circumference(self):
        """Return the circumference of the circle"""
        return (2 * pi * self.__radius)
