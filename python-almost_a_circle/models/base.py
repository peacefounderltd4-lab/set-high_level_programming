
#!/usr/bin/python3
import csv

"""This module defines the Base class."""


class Base:
    """Base class for managing IDs."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
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
        """Load objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
        except FileNotFoundError:
            return []

        instances = []
        for row in rows:
            values = [int(value) for value in row]
            if cls.__name__ == "Rectangle":
                obj = cls(
                    values[1], values[2],
                    values[3], values[4], values[0]
                )
            elif cls.__name__ == "Square":
                obj = cls(
                    values[1], values[2], values[3], values[0]
                )
            else:
                continue
            instances.append(obj)
        return instances
        
