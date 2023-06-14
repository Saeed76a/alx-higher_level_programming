#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    new_mat = [[0] * len(k) for k in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_mat[i][j] = matrix[i][j]**2
    return new_mat
