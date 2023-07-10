#!/usr/bin/python3
"""
4. Only sub class of
"""


def inherits_from(obj, a_class):
    """
    declare a function that check if the
    object is an sub of class

    Args:
        obj (onj): the object to check
        a_class (class): the class
    Return:
        True
        False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
