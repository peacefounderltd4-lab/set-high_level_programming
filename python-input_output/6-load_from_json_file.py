#!/usr/bin/python3
"""
Defines a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None
