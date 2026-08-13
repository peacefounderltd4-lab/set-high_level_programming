#!/usr/bin/python3
"""Module for converting a class instance to a dictionary."""


def class_to_json(obj):
    """Return the dictionary representation of a class instance."""
    return obj.__dict__
