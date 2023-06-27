#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """representing square operation"""
    def __init__(self, size=0):
        """intialize the square
        Args:
            size (int): The size of the square
        """
        self.size = size

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set the size
        Args:
            value (int): The value of the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
