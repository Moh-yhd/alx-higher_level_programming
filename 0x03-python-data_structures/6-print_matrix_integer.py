#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end="\n" if j == i[-1] else " ")
