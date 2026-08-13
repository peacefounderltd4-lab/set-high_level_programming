#!/usr/bin/python3
"""Module to read a text file."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
