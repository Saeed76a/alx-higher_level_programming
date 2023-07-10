#!/usr/bin/python3
"""
3. Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
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
    return isinstance(obj, a_class)
