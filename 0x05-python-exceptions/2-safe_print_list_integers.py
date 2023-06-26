#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    if my_list:
        for i in range(x):
            try:
                try:
                    print("{:d}".format(my_list[i]), end='')
                    i += 1
                except (TypeError, ValueError):
                    continue
            except IndexError:
                break
    print("\n", end='')
    return i