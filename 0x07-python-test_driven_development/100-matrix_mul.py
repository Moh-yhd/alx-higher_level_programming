#!/usr/bin/python3
"""
    The "100-matrix_mu" module
    The module only has one function: matrix_mul

"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices if they are multipliable
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    width = len(m_a[0])
    for row in m_a:
        if len(row) != width:
            raise TypeError("each row of m_a must be of the same size")
    width = len(m_b[0])
    for row in m_b:
        if len(row) != width:
            raise TypeError("each row of m_b must be of the same size")
    rowM_a = len(m_a[0])
    colM_b = len(m_b)
    if rowM_a != colM_b:
        raise ValueError("m_a and m_b can't be multiplied")

    mat_list = matrix_to_list(m_b)

    mul_res = []
    for i in range(len(m_a)):
        mul_row = []
        for j in range(len(mat_list)):
            mul = 0
            k = 0
            for m in range(len(mat_list[j])):
                mul += m_a[i][k] * mat_list[j][m]
                k += 1
            mul_row.append(mul)
        mul_res.append(mul_row)
    return (mul_res)


def matrix_to_list(m_b):
    """Changes colums of a matrix into rows
    """
    r = len(m_b)
    c = len(m_b[0])
    mat_list = []
    for i in range(c):
        row = []
        for j in range(r):
            elem = m_b[j][i]
            row.append(elem)
        mat_list.append(row)
    return (mat_list)
