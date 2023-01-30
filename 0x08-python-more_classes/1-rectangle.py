#!/usr/bin/python3
"""Defines a class called Rectangle"""


class Rectangle:
    """Creates a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the width and height of class rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private instance atrribut width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height varible"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
