#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square attribute
    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Sets attributes
        Args:
            size (int): thr size of the square
            position (tuple) the coordinates of center of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets the position of the square
        Return:
            None
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the coordinate position of a square
        Args:
            value (int): coordinate of the squaere
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2\
        or type(value[0]) is not int or type(value[1]) is not int or\
        value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of a square and returns it"""
        return (self.__size)**2

    def my_print(self):
        """Prints the square using '#'
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('_'*self.position[0], end="")
            for j in range(self.__size):
                print('#', end="")
            print()
