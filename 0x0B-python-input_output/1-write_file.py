#!/usr/bin/python3
"""Write file module. Contains a function that writes on a file"""


def write_file(filename="", text=""):
    """Writes text on a file.
        Args:
            filename: naame of file where text is to be written

            text: text to be written
        Return: number of charachters written

    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        write_data = my_file.write(text)
        return my_file
