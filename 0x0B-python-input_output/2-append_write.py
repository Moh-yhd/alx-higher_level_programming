#!/usr/bin/python3
"""append write file module. Contains a function that writes on a file"""


def append_write(filename="", text=""):
    """Appends text on a file.
        Args:
            filename: name of file where text is to be appended

            text: text to be written
        Return: number of charachters appended

    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
