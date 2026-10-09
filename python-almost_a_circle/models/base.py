#!/usr/bin/python3
"""Base class for all models."""
import json


class Base:
    """Manage the id attribute of all models."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        dictionaries = [
            obj.to_dictionary() for obj in list_objs
        ]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return a list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with attributes already set."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            raise TypeError("Unsupported class")

        instance.update(**dictionary)
        return instance
