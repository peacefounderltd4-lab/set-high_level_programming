#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student."""
        if attrs is None:
            return self.__dict__

        return {
            key: getattr(self, key)
            for key in attrs
            if key in self.__dict__
        }
