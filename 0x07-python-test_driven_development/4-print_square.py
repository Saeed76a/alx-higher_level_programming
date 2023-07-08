#!/usr/bin/python3
"""
prints a square
"""


def print_square(size):
    """
    prints a square of #
    Args:
        size (int): size of square
    Raise:
        TypeError with message
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
