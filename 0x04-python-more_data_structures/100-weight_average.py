#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        add2 = 0
        num = 0
        result = 0
        for _tuple_ in my_list:
            add2 += _tuple_[1]
            num += _tuple_[0] * _tuple_[1]
        result = num / add2
        return result
    return 0
