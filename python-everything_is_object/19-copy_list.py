#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """A class that restricts new attribute creation."""

    __slots__ = ["first_name"]
    
