#!/usr/bin/python3
"""
 5. To JSON
"""
import json
"""
get json module
"""


def save_to_json_file(my_obj, filename):
    """
    function that returns the JSON
    representation of an object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
