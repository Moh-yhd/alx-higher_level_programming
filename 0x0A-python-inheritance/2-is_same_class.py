#!/usr/bin/python3
""" The is_same_class module"""


def is_same_class(obj, a_class):
    """ checks if an object is an exact instance of a class
        Args:
            obj: object
            a_class: class
    """
    obj_list = dir(obj)
    class_list = dir(a_class)
    for elem in obj_list:
        if elem not in class_list:
            return False
    return True
