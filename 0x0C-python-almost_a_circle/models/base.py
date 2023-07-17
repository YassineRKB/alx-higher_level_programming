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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method: dictonaries to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            res = dumpjs(list_dictionaries)
        return res

    @staticmethod
    def from_json_string(json_string):
        """method: dictonaries to json"""
        if json_string is None:
            return []
        else:
            res = loadjs(json_string)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        """method: save_to_file"""
        dicList = []
        if list_objs is not None:
            for item in list_objs:
                dicList.append(item.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, "w") as w:
            w.write(f"{cls.to_json_string(dicList)}")
