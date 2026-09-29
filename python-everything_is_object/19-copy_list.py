#!/usr/bin/python3
"""LockedClass module."""


class LockedClass:
    """A class that prevents dynamic attribute creation
    except for first_name.
    """
    __slots__ = ["first_name"]
    
