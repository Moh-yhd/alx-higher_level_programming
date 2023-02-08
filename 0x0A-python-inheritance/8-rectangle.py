#!/usr/bin/python3
""" The base_geometry module"""


class BaseGeometry:
    """ Creates a class BaseGeometry"""
    def area(self):
        " Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Creates a class rectangle"""
    def __init__(self, width, height):
        """ Initializes self """
        self.__width = width
        BaseGeometry.integer_validator(self, "width", width) 
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height) 

