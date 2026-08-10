#!/usr/bin/python3
"""Add 2 integers."""


def add_integer(a, b=98):
    """Return the addition of a and b as integers."""
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
