#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a simple function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
