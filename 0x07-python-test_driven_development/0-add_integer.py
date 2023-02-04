#!/usr/bin/python3
"""
    The "0-add_integer" module
    The module only has one function, add(a, b)

"""


def add_integer(a, b=98):
    """ Addition function
        Adds two int or float numbers and return the value
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
