#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda i: list(map(lambda j: j * j, i)), matrix))
    return new_matrix
