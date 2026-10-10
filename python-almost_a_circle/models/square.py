#!/usr/bin/python3
"""Icyiciro cya Square gikomoka kuri Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class ikoresha uburebure bungana kuri width na height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Gutangiza Square object."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gufata uburebure bwa size."""
        return self.width

    @size.setter
    def size(self, value):
        """Gushyiraho size ku mpande zombi."""
        self.width = value
        self.height = value

    def __str__(self):
        """Inyandiko yerekana imiterere ya Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Ivugurura attributes za Square."""
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Igarura dictionary representation ya Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
    }
        
