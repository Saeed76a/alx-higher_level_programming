#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        list = []
        list += my_list
        list[idx] = element
        return list
    return my_list
