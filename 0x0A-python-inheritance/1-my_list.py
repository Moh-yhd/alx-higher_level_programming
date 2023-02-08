#!/usr/bin/python3
""" The My_list module """


class MyList(list):
    """Creates a class that inherites the list class """
    def __init__(self):
        """ Inherit class """
        super().__init__()

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
