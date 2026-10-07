#!/usr/bin/python3
"""
Module yirimo umuseke load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """
    Atekereza hanyuma akarema Python object ivuye muri idosiye ya JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
