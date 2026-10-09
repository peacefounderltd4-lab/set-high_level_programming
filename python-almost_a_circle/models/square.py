#!/usr/bin/python3
"""Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the square description."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    def update(self, *args, **kwargs):
        """Assign square attributes."""
        attributes = ["id", "size", "x", "y"]

        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
