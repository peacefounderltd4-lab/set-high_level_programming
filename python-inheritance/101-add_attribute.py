#!/usr/bin/python3
"""Module containing a function to add attributes to objects."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object when possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
