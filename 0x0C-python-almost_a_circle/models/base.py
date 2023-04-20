#!/usr/bin/python3
"""Contains a Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            list_objs = []
        list_objs = [ob.to_dictionary() for ob in list_objs]
        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
