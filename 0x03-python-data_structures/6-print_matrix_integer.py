#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    m = len(matrix)
    for i in range(len(matrix)):
        n = len(matrix[i])
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j < n - 1:
                print(" ", end=" ")
            if j == n - 1 and i != m - 1:
                print()
    print()
