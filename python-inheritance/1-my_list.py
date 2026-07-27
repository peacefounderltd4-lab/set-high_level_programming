#!/usr/bin/python3
"""Module containing the MyList class."""


class MyList(list):
    """A custom list class with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
