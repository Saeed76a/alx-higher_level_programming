#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 1 and b > 1:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    if a == 0 and b > 1:
        return (tuple_b)
    if b == 1 and a > 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    if b == 0 and a > 1:
        return (tuple_a)
    if a == 1 and b == 1:
        return (tuple_a[0] + tuple_b[0], 0)
    if a == 0 and b == 1:
        return (tuple_b[0], 0)
    if a == 1 and b == 0:
        return (tuple_a[0], 0)
    if a == 0 and b == 0:
        return (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
