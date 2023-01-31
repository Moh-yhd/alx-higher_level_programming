#!/usr/bin/python3
"""
    The "2-matrix_divided.py" module
    The module only has one function "matrix_divided"

"""


def matrix_divided(matrix, div):
    """ Matrix dividing function
        Divides each elements of a matrix by a number
        Returns the division resulti as a matrix
    """
    for row1 in matrix:
        for row2 in matrix:
            if len(row1) != len(row2):
                raise TypeError("Each row of the "
                                "matrix must have the same size")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
    for row in matrix:
        for num in row:
            if type(num) not in (int, float):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = []
    for row in matrix:
        div_list = []
        for num in row:
            result = round(num / div, 2)
            div_list.append(result)
        div_matrix.append(div_list)
    return div_matrix
