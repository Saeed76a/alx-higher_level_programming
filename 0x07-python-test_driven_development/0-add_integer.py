#!/usr/bin/python3
"""
    add_integer - Adds two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default value is 98.
    Returns: the addition of a and b.
    Raises: TypeError with message if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, int):
        a = int(a)
    if not isinstance(b, int):
        b = int(b)
    return (a + b)
