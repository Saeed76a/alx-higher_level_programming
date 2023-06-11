#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    new_list += my_list
    for i in range(len(my_list)):
        new_list[i] = my_list[i] % 2 == 0
    return new_list
