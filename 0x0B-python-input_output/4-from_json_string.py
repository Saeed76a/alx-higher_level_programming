#!/usr/bin/python3
"""
 4. From JSON string to Object
"""
import json
"""
hello json
"""


def from_json_string(my_str):
    """
    function that returns an object
    """
    return json.loads(my_str)
