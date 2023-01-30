#!/usr/bin/python3
"""Defines a class called Rectangle"""


class Rectangle:
    """Creates a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the width and height of class rectangle"""
        self.__height = height
        self.__width = width

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

    def area(self):
        """Returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns the rectangle using #"""
        if self.__width == 0 and self.__height == 0:
            return ""
        pr = ""
        pr += "\n".join("#" * self.__width for j in range(self.__height))
        return pr

    def __repr__(self):
        """returns a string representation of the Rectangle for reuse"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delets an instance of a rectangle"""
        print("Bye rectangle...")
