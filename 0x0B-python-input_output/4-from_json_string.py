#!/usr/bin/python3
"""The Json_strng Module: contains the from_json_string function"""
import json


def from_json_string(my_str):
    """Creates a json representation of  string
    Args:
        my_str: string to be converted to json

    Return: json repesentation of a string

    """
    return json.loads(my_str)
