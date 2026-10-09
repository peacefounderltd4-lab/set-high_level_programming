#!/usr/bin/python3
"""Unit tests for Base."""
import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_id(self):
        obj = Base(12)
        self.assertEqual(obj.id, 12)

    def test_generated_id(self):
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        data = [{"id": 1}]
        result = Base.to_json_string(data)
        self.assertEqual(json.loads(result), data)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        data = [{"id": 1}]
        result = Base.from_json_string(json.dumps(data))
        self.assertEqual(result, data)

    def test_save_to_file(self):
        rect = Rectangle(4, 5)
        filename = "Rectangle.json"

        try:
            Rectangle.save_to_file([rect])

            with open(filename, encoding="utf-8") as file:
                data = json.load(file)

            self.assertEqual(data, [rect.to_dictionary()])
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_create_rectangle(self):
        original = Rectangle(4, 5, 2, 1, 10)
        created = Rectangle.create(**original.to_dictionary())
        self.assertEqual(str(created), str(original))

    def test_create_square(self):
        original = Square(5, 2, 1, 10)
        created = Square.create(**original.to_dictionary())
        self.assertEqual(str(created), str(original))


if __name__ == "__main__":
    unittest.main()
