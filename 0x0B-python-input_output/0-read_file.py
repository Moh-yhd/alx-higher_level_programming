#!/usr/bin/python3
""" A script that opens and reads a file """


def read_file(filename=""):
    """Opens a file, reads it and prints its content

    Args:
        filename: filename to be read

    """
    with open(filename, encoding="utf-8") as my_file:
        file_read = my_file.read()
        print(file_read)
