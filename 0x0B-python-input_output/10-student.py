#!/usr/bin/python3
"""
9. Student to JSON
"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize the object with the provided arguments.

        Args:
            first_name (str): student's first name.
            last_name (str): student's last name.
            age (int): the age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        get the dictionary description
        with simple data structure

        Args:
            attrs (list): list of attributes
        """
        my_dict = {}
        if attrs is not None:
            for attr in attrs:
                try:
                    my_dict[attr] = self.__dict__[attr]
                except Exception:
                    pass
        else:
            return self.__dict__
        return my_dict
