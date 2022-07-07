#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    if len(matrix) > 0:
        for row in matrix:
            n_matrix.append(list(map(lambda x: x**2, row)))
    return n_matrix
