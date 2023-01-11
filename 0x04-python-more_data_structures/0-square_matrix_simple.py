#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_matrix = matrix.copy()
    for i in range(len(matrix)):
        res_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))

    return res_matrix
