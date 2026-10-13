
#!/usr/bin/python3
"""This module defines the Base class."""

import csv
import json


class Base:
    """Base class for managing IDs and serialization."""

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
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write objects to a JSON file."""
        filename = cls.__name__ + ".json"
        dictionaries = []
        if list_objs is not None:
            dictionaries = [obj.to_dictionary() for obj in list_objs]

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
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**item) for item in dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save instances to a CSV file."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            if list_objs is None:
                return

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id, obj.width, obj.height, obj.x, obj.y
                    ])
                elif cls.__name__ == "Square":
                    writer.writerow([
                        obj.id, obj.size, obj.x, obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file."""
        filename = cls.__name__ + ".csv"

        try:
            with open(
                filename, "r", newline="", encoding="utf-8"
            ) as csvfile:
                rows = list(csv.reader(csvfile))
        except FileNotFoundError:
            return []

        instances = []

        for row in rows:
            values = [int(value) for value in row]

            if cls.__name__ == "Rectangle":
                instance = cls(
                    values[1], values[2], values[3], values[4], values[0]
                )
            elif cls.__name__ == "Square":
                instance = cls(
                    values[1], values[2], values[3], values[0]
                )
            else:
                continue

            instances.append(instance)

        return instances
        
