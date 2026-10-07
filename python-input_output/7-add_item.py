#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file named add_item.json.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists, otherwise initialize an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Append all command-line arguments (excluding script name sys.argv[0])
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, filename)
