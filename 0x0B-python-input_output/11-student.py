#!/usr/bin/python3
"""Module student"""


class Student:
    """student class"""

    def __init__(self, firstname, lastname, age):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self, attr=None):
        dicct = {}
        if type(attr) is list:
            for attribute in attr:
                if type(attribute) is not str:
                    break
                if hasattr(self, attribute):
                    dicct[attribute] = getattr(self, attribute)
            return dicct
        return self.__dict__

    def reload_from_json(self, json):
        for attribute in json:
            value = json[attribute]
            setattr(self, attribute, value)
