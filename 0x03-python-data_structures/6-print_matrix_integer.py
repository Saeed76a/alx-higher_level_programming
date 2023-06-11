#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        for i in matrix:
            for j in i:
                print("{:d}".format(j),
                      end=' ' if j != i[len(i) - 1] else '\n')
    else:
        print("".format())
