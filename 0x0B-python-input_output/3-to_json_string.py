#!/usr/bin/python3
"""
 3. To JSON string
"""
import json
"""
get json module
"""


def to_json_string(my_obj):
    """
    function that returns the JSON
    representation of an object
    """
    return json.dumps(my_obj)
