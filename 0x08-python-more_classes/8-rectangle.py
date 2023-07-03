#!/usr/bin/python3
"""declare the Rectangle class"""


class Rectangle:

    """Public class attributes"""
    print_symbol = "#"
    number_of_instances = 0
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the class
        Args:
            width (int): the width of rectangle
            height (int): the height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """detect if rectangle delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
