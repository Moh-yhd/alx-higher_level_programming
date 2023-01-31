#!/usr/bin/python3
"""
    This is the "4-print_square.py" module
    The module onle has the print_square function

"""


def print_square(size):
    """ Prints the square of size 'size' using '#'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
