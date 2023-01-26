#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square attribute
    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size=0):
        """Validating the size of a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a square and returns it"""
        return (self.__size)**2
