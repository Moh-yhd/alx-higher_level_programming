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

    @property
    def size(self):
        """getter of size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of the size of a square
    Args:
        value type int: size of the square
    Returns:
        None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of a square and returns it"""
        return (self.__size)**2

    def my_print(self):
        """Prints the square using '#'
        Returns:
            None
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
