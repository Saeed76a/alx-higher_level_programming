#!/usr/bin/python3
"""
11. square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialize the object with the provided arguments.

        Args:
            size (int): the size of the squre
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the square"""
        return self.__size ** 2

    def __str__(self):
        """ the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
