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
        typeAttr = isinstance(attr, list)
        if typeAttr:
            for attribute in attr:
                if type(attribute) is not str:
                    break
                if hasattr(self, attribute):
                    dicct[attribute] = getattr(self, attribute)
            return dicct
        return self.__dict__
