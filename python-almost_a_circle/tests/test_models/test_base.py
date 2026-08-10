#!/usr/bin/python3
"""Test Base class."""

import json
import os
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base."""

    def setUp(self):
        """Reset object counter."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test automatic IDs."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test custom ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_json_none(self):
        """Test JSON with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_json_empty(self):
        """Test JSON with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_json(self):
        """Test JSON conversion."""
        data = [{"id": 1, "width": 2}]
        result = Base.to_json_string(data)
        self.assertEqual(json.loads(result), data)

    def test_from_json_none(self):
        """Test JSON to list with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test JSON to list with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json(self):
        """Test JSON to list."""
        data = [{"id": 1}]
        result = Base.from_json_string(json.dumps(data))
        self.assertEqual(result, data)

    def test_save_load(self):
        """Test JSON save and load."""
        from models.rectangle import Rectangle

        objects = [Rectangle(4, 5, 1, 2)]
        Rectangle.save_to_file(objects)
        loaded = Rectangle.load_from_file()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(),
                         objects[0].to_dictionary())

        os.remove("Rectangle.json")

    def test_load_missing(self):
        """Test missing JSON file."""
        from models.rectangle import Rectangle

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create(self):
        """Test create."""
        from models.rectangle import Rectangle

        data = {
            "id": 89,
            "width": 10,
            "height": 4,
            "x": 2,
            "y": 3
        }

        rect = Rectangle.create(**data)
        self.assertEqual(rect.to_dictionary(), data)

    def test_csv(self):
        """Test CSV save/load."""
        from models.rectangle import Rectangle

        objects = [Rectangle(10, 7, 2, 8)]
        Rectangle.save_to_file_csv(objects)

        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(
            loaded[0].to_dictionary(),
            objects[0].to_dictionary()
        )

        os.remove("Rectangle.csv")


if __name__ == "__main__":
    unittest.main()
