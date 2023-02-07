#!/usr/bin/python3
"""The Json Sting Moudule: contains the to_json_string(my_obj) function"""
import json


def to_json_string(my_obj):
    """Returns the json represntation of a string.
    Args:
        my_obj: object

    """
    return json.dumps(my_obj)
