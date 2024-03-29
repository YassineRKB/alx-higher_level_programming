#!/usr/bin/python3
"""Model for base class"""
from os import path
from json import dumps as dumpjs
from json import loads as loadjs
import csv
import turtle

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

    @classmethod
    def create(cls, **dictionary):
        """method: create"""
        cname = cls.__name__
        if cname != "Rectangle":
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """method: load from file"""
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, "r") as r:
            lines = r.read()
        res = []
        for line in cls.from_json_string(lines):
            res.append(cls.create(**line))
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method: save_to_file_csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as w:
            towrite = csv.writer(w)
            for obj in list_objs:
                if filename == "Rectangle.csv":
                    dicc = [obj.id, obj.width, obj.height, obj.x, obj.y]
                else:
                    dicc = [obj.id, obj.size, obj.x, obj.y]
                towrite.writerow(dicc)

    @classmethod
    def load_from_file_csv(cls):
        """method: load_from_file_csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as r:
            toread = csv.reader(r)
            res = []
            list = {}
            rect = ["id", "width", "height", "x", "y"]
            squa = ["id", "size", "x", "y"]
            fieldnames = rect if filename == "Rectangle.csv" else squa
            for row in toread:
                instance = cls.create(
                    **{key: int(value) for key, value in zip(fieldnames, row)}
                    )
                res.append(instance)
            return res

    @staticmethod
    def draw(list_rectangles, list_squares):
        """method: draw"""
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        colors = ["blue", "orange", "green", "red", "white"]
        ran = 0
        t.color(colors[ran])
        t.penup()
        t.goto(-200, 200)
        for rectangle in list_rectangles:
            if ran == 4:
                ran = 0
            else:
                ran += 1
            t.color(colors[ran])
            t.goto(t.xcor() + (rectangle.width + 40), t.ycor() - (rectangle.height + 80))
            t.up()
            t.down()
            for i in range(2):
                if ran == 4:
                    ran = 0
                else:
                    ran += 1
                t.color(colors[ran])
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.penup()
        t.goto(-200, -50)
        for square in list_squares:
            if ran == 4:
                ran = 0
            else:
                ran += 1
            t.color(colors[ran])
            t.goto(t.xcor() + (square.width + 10), t.ycor() - (square.height + 40))
            t.up()
            t.down()
            for i in range(2):
                if ran == 4:
                    ran = 0
                else:
                    ran += 1
                t.color(colors[ran])
                t.forward(square.width)
                t.left(90)
                t.forward(square.height)
                t.left(90)
            t.penup()
        turtle.done
