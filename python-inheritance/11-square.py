#!/usr/bin/python3
"""Module containing the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
