#!/usr/bin/python3
""" The base_geometry module"""


class BaseGeometry:
    """ Creates a class BaseGeometry"""
    def area(self):
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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Prints representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
