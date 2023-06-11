#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is not None:
        for i in matrix:
            for j in i:
                print("{}".format(j), end=' ' if j != i[len(i) - 1] else '\n')
    else:
        print()
