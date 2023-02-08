#!/usr/bin/python3
""" The is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """ checks if an object is an exact instance of a class
        Args:
            obj: object
            a_class: class
    """
    return isinstance(obj, a_class)
