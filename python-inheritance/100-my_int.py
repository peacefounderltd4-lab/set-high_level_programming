#!/usr/bin/python3
"""Module containing the MyInt class."""


class MyInt(int):
    """A rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """Return the opposite of the normal equality comparison."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return the opposite of the normal inequality comparison."""
        return int.__eq__(self, other)
