#!/usr/bin/python3
"""
8. Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits
    from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Rectangle Instantiation

        Args:
            width (int): the width
            height (int): the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__hieght = height
