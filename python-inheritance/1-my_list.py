#!/usr/bin/python3
"""Module containing the MyList class."""


class MyList(list):
    """A list subclass with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
