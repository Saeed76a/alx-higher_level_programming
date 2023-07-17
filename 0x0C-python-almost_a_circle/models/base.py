#!/usr/bin/python3
"""
The Base class serves as the base class
for other classes in the project.
"""
import json


class Base:
    """
    This class will be the “base” of
    all other classes in this project.

    description:
        manage id attribute in all
        my future classes
    class attribute:
        private:
            __nb_objects (int)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the object with the provided arguments.

        Args:
            id (int): attribute's id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the string object of an list dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of objects/anstances to a file
        """
        with open("{}.json\
".format(cls.__name__), 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_list = []
                for i in list_objs:
                    json_list.append(i.to_dictionary())
                file.write(Base.to_json_string(json_list))
