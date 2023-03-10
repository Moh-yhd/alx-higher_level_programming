#!/usr/bin/python3
""" The is_same_class module"""


def is_same_class(obj, a_class):
    """ checks if an object is an exact instance of a class
        Args:
            obj: object
            a_class: class
    """
    return (type(obj) == a_class)
