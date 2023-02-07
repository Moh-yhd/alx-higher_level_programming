#!/usr/bin/python3
"""The Json_file Module: contains the save_to_json"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object on to a text file using json representation
    Args:
        my_obj: object whose json representation is to be written on a file

        filename: text file to be written on

    """
    with open(filename, 'w', encoding='utf-8') as my_file:
       json.dump(my_obj, my_file)
