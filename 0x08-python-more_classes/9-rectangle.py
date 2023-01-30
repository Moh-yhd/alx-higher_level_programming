#!/usr/bin/python3
"""Defines a class called Rectangle"""


class Rectangle:
    """Creates a class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the width and height of class rectangle"""
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """Compares two rectangles and returns the bigger one
            Args:
                rect_1 (int): instance of rectangle one
                rect_2 (int): instance of rectangle two
            Returns:
                instance of bigger area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Defines a square class with"""
        return cls(size, size)

    def __str__(self):
        """returns the rectangle using #"""
        if self.__width == 0 and self.__height == 0:
            return ""
        pr = ""
        pr += "\n".join(str(self.print_symbol) * self.__width
                        for j in range(self.__height))
        return pr

    def __repr__(self):
        """returns a string representation of the Rectangle for reuse"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delets an instance of a rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
