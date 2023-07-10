#!/usr/bin/python3
"""
function:
    that returns True if the object is
    exactly an instance of the specified class ;
    otherwise False.
"""


def is_same_class(obj, a_class):
    """
    declare a function that check if the
    object is an anstance of class

    Args:
        obj (onj): the object to check
        a_class (class): the class
    Return:
        True
        False
    """
    return type(obj) == a_class
