#!/usr/bin/python3
"""Icyiciro cya Rectangle gisangiye ibintu na Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class ifite width, height, x, na y."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Gutangiza Rectangle object."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gufata agaciro ka width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Gushyiraho agaciro ka width n'igenzura."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gufata agaciro ka height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Gushyiraho agaciro ka height n'igenzura."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gufata agaciro ka x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Gushyiraho agaciro ka x n'igenzura."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gufata agaciro ka y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Gushyiraho agaciro ka y n'igenzura."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Ibarura ubuso (area) bwa Rectangle."""
        return self.width * self.height

    def display(self):
        """Yerekana Rectangle ikoresheje ikimenyetso cya '#'."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Inyandiko yerekana imiterere ya Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Ivugurura attributes za Rectangle."""
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Igarura dictionary representation ya Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
    }
    
