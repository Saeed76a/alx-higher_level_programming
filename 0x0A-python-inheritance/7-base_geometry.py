#!/usr/bin/python3
"""
7. Integer validator
"""


class BaseGeometry:
    """declare an class BaseGeometry"""

    def area(self):
        """
        Public instance method:

        Raise:
            Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method:

        function: that validate a value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
