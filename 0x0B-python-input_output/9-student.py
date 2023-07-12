#!/usr/bin/python3
"""Module student"""


class Student:
    """student class"""

    def __init__(self, firstname, lastname, age):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self):
        return self.__dict__
