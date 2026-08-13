#!/usr/bin/python3
"""Add command-line arguments to a JSON file."""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Load items, add command-line arguments, and save them."""
    try:
        items = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
