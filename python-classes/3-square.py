#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square."""
        return self.__size ** 2
