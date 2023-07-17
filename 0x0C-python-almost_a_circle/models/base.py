#!/usr/bin/python3
"""Model for base class"""
from os import path
from json import dumps as dumpjs
from json import loads as loadjs


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method: dictonaries to json"""
        if list_dictionaries is None or \
            type(list_dictionaries) != list \
                or len(list_dictionaries) == 0:
            return "[]"
        return  dumpjs(list_dictionaries)
