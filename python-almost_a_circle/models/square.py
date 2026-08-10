#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """Update Square attributes."""
        if args:
            attributes = ["id", "size", "x", "y"]

            for index, value in enumerate(args):
                if index >= len(attributes):
                    break
                setattr(self, attributes[index], value)
            return

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
