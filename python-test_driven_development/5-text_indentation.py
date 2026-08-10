#!/usr/bin/python3
"""Text indentation."""


def text_indentation(text):
    """Print text with two new lines after ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    line = ""

    for char in text:
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
        else:
            line += char

    if line.strip():
        print(line.strip(), end="")
