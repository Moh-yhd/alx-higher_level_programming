#!/usr/bin/python3
"""A script that opens and reads a file
"""


def read_file(filename=""):
    """Opens a file, reads it and prints its content"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
