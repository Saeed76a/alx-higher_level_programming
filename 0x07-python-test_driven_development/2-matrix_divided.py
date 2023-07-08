#!/usr/bin/python3
"""
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Args:
        matrix (list): divides all elements of a matrix.
        div (int): a number
    Return:
        new matrix
    Raise:
        TypeError with missage
        ZeroDivisionError with missage
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[]]
    new_matrix = [[0] * len(k) for k in matrix]
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if i != 0 and checklen != len(matrix[i]):
            raise TypeError("Each row of the matrix must have \
the same size")
        checklen = len(matrix[i])
        for j in range(checklen):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix
