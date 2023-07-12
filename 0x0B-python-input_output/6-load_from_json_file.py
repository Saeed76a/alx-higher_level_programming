#!/usr/bin/python3
"""
 6 From JSON string to Object
"""
import json
"""
hello json
"""


def load_from_json_file(filename):
    """
    function that returns an object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
