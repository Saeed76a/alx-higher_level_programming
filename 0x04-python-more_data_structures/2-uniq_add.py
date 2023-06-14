#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    n = 0
    new_list = [[0] for k in my_list]
    for i in my_list:
        f = 0
        for j in range(len(new_list)):
            if i == new_list[j]:
                f = 1
        if f == 0:
            new_list[n] = i
            sum += i
            n += 1
    return sum
