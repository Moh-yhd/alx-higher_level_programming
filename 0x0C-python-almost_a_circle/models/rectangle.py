#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Creates a Rectangle class. It inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing attributes of the a Rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinates of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of the x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinates of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of the y coordinates"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Displays the rectangle using '#' charachter"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * ' ', end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns the string format of the instance """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the class Rectangle """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) > 0:
            attrib = ["id", "width", "height", "x", "y"]
            try:
                for i, arg in enumerate(args):
                    setattr(self, attrib[i], arg)
            except IndexError:
                pass

    def to_dictionary(self):
        """Returns the dictionary represetation of a rectangle"""
        return {'id': self.id, 'height': self.height,
                'width': self.width, 'x': self.x, 'y': self.y}
