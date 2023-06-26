#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    if my_list:
        for num in range(x):
            try:
                print("{:d}".format(my_list[num]), end='')
                i += 1
            except (TypeError, ValueError):
                continue
    print("\n", end='')
    return i
