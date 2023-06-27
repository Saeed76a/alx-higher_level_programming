#!/usr/bin/python3
from math import pi
class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if not isinstance(raduis, int) and not isinstance(raduis, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius
        return self.__radius
    def area(self):
        return (self.__radius **2 * pi)
    def circumference(self):
        return (2 * pi * self.__radius)
