#!/usr/bin/python3
"""Module containing a function that checks class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an inherited instance of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
