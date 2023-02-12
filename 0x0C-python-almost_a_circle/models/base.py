#!/usr/bin/python3
"""The base module """
import json


class Base:
    """The base of all classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing
            Args
                id: id of objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON rpresentation of a class instance
        on a file
        """
        filename = cls.__name__ + ".json"
        json_dictionaries = []
        if list_objs:
            for obj in list_objs:
                json_dictionaries.append(obj.to_dictionary())
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(Base.to_json_string(json_dictionaries))
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON sring representation"""
        if json_string == None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(4, 4)
            else:
                dummy = cls(4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        created_list = []
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                dict_list = Base.from_json_string(f.read())
                for dictionary in dict_list:
                    created_list.append(cls.create(**dictionary))
        return created_list
