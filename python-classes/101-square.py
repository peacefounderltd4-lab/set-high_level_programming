#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print(self.__str__(), end="")

    def __str__(self):
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]

        for i in range(self.__size):
            result += (" " * self.__position[0] +
                       "#" * self.__size)

            if i != self.__size - 1:
                result += "\n"

        return result
