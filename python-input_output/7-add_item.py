#!/usr/bin/python3
"""Iyi script yongeza ibintu byose byatanzwe mu murongo w'amabwiriza

(command line arguments) mu rutonde rwa Python, hanyuma ikabibika
mu dosiye ya JSON yitwa `add_item.json`.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
￼Enter
