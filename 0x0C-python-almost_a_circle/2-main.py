#!/usr/bin/python3

from models.rectangle import Rectangle

if __name__ == "__main__":
    try:
        r1 = Rectangle(10, 'df')
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    print("--------------")
    try:
        r = Rectangle({"f":4}, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print("--------------")
    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print("--------------")
    try:
        Rectangle('kl', 2, 0, 1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

