#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 2)
    print(r1.id)
    print("width = ", r1.width)
    print("height = ", r1.height)

    r2 = Rectangle(2, 10)
    print(r2.id)
    print("width = ", r2.width)
#   print(r2.height)

    r3 = Rectangle(10, 2, 10, 20, 12)
    print(r3.id)
    print("width = ", r3.width)
    print(r3.x)
    print(r3.y)
