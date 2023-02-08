#!/usr/bin/python3
""" The inherits_from module"""


def inherits_from(obj, a_class):
    """ checks if an object is an object is a subclass
        Args:
            obj: object
            a_class: class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
