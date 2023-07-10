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
    sorted_list = []

    def print_sorted(self):
        MyList.sorted_list += self
        print(sorted(MyList.sorted_list))
