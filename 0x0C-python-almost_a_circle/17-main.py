#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
    r3 = Square(1, 5, 6)
    r3_dictionary = r3.to_dictionary()
    r4 = Square.create(**r3_dictionary)
    print(r3)
    print(r4)
    r5 = [1, 2, 3]
    r5_dictionary = r5.to_dictionary()
    r6 = Rectangle.create(**r5_dictionary)

