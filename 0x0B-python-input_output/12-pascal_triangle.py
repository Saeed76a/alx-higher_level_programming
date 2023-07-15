#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    get a list of lists of integers
    representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    list_ratuened = []
    listen = []
    for i in range(n):
        v = []
        for j in range(i + 1):
            if i is j or j is 0 or i is 0:
                v.append(1)
            else:
                v.append(listen[j] + listen[j - 1])
        listen = v
        list_ratuened.append(v)
    return list_ratuened
