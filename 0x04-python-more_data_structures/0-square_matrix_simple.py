#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix
    new_matrix = []
    for a_list in matrix_cpy:
        sq_list = list(map(lambda x: x * x, a_list))
        new_matrix.append(sq_list)

    return new_matrix
