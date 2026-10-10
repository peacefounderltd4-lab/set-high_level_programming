#!/usr/bin/python3
"""Icyiciro cy'ibanze (Base class) gihuriweho n'izindi class zose."""
import json


class Base:
    """Class ifite inshingano yo gucunga no kuringaniza id n'imikorere ya JSON."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Gutangiza Base object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Igarura JSON string representation ya list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Iandika JSON string representation ya list_objs muri dosiye."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [o.to_dictionary() for o in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Igarura list y'ibiri muri JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Igarura object yuzuye ifite attributes zose zatanzwe."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Igarura list y'objects zisomwe muri dosiye."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
            
