#!/usr/bin/python3
import json
"""
The Base class serves as the base class
"""


class Base:
    """
    This class will be the “base” of
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the object with the provided arguments.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        return the string object of an list dictionaries
        """
        return json.dumps(list_dictionaries)

#     @classmethod
#     def save_to_file(cls, list_objs):
#         with open("{}.json\
# ".format(cls.__class__.__name__), 'w', encoding="utf-8") as file:
#             file.write(cls.to_json_string(list_objs))
