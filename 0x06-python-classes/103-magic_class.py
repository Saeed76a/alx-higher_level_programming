#!/usr/bin/python3
"""define the Python class MagicClass that does exactly the same\
      as the following Python bytecode:"""
import math


class MagicClass:
    """set a circle"""

    def __init__(self, radius):
        """intialize MagicClass:
        Args:
            radius (float and int): the raduis of the circle
        """
        self.__radius = 0
        if not isinstance(raduis, int) and not isinstance(raduis, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius
        """Return the current radius"""
        return self.__radius

    def area(self):
        """Return the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the circle"""
        return (2 * math.pi * self.__radius)
