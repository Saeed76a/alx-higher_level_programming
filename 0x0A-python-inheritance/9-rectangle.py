#!/usr/bin/python3
"""
9. Full rectangle
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
        self.__height = height

    def area(self):
        """
        Rectangle area

        Return:
            an area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return:
            the following rectangle description:
            [Rectangle] <width>/<height>
        """
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
