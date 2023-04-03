#!/usr/bin/python3
""" This module defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide elements in a matrix
    Args:
        matrix: list of lists of integers or floats
        div: divisor
    Return:
        new matrix
    """

    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")

    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
