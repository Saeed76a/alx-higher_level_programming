#!/usr/bin/python3
"""
1. My list
class:
    that inherits from list:
"""


class MyList(list):
    """
    declare a class MyList
    that inherits from list
    """
    def print_sorted(self):
        sorted_list = []
        sorted_list += self
        print(sorted(sorted_list))
    pass
