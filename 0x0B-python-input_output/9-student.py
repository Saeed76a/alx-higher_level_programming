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

    def to_json(self):
        """
        get the dictionary description
        with simple data structure
        """
        return self.__dict__
