#!/usr/bin/python3
from turtle import Turtle, Screen
import csv
import json

"""
This provides a way to generate unique
identifiers (UUIDs) for objects
"""

import uuid

"""
Base is a perent class with a private class attribute
Attribute:
    __nb_objects
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This initialize the class Base by id
        Attribute:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """
    This i a function that return the JSON string
    representation of dictionaries
    Arguments:
        list_dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Checks list_dictionaries
        Return:
            []
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    """
    This is a function that Write the JSON string
    representation of list_objs to a file
    Arguments:
        cls
        list_objs
    """
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        json_data = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_data)

    """
    This function return list of  the JSON string
    representation of json_string
    Arguments:
        json_string
    """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    """
    This is a class method  that returns an instance
    with all attributes already set
    Arguments:
        cls
        dictionary
    """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    """
    This is a class method that returns a list of instances
    Arguments:
        cls
    Return:
        []
    """
    @classmethod
    def load_from_file(cls):
        """
        Try file and return an empty list
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_dicts = cls.from_json_string(json_data)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []
    """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_dict())

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instance_dict = cls.from_csv_dict(row)
                    instance = cls.create(**instance_dict)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = Screen()
        screen.bgcolor("white")

        for rect in list_rectangles:
            t = Turtle()
            t.penup()
            t.speed(2)
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squsres:
            t = Turtle()
            t.penup()
            t.speed(2)
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.exitonclick()
        """
