#!/usr/bin/python3
""" The Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class based on Rectangle Class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises a Square class """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ Gets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the value of thei size of the square """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the class Square """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) > 0:
            attrib = ["id", "size", "x", "y"]
            try:
                for i, arg in enumerate(args):
                    setattr(self, attrib[i], arg)
            except IndexError:
                pass

    def __str__(self):
        """ Returns the string format of the instance """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns the dictionary represetation of a rectangle"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
