
#!/usr/bin/python3
"""Unit tests for the Almost a Circle project."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_base_id(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_base_auto_id(self):
        base = Base()
        self.assertIsInstance(base.id, int)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_rectangle_creation(self):
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 3)
        self.assertEqual(rectangle.area(), 12)

    def test_invalid_width_type(self):
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Rectangle("4", 3)

    def test_invalid_height_value(self):
        with self.assertRaisesRegex(
                ValueError, "height must be > 0"):
            Rectangle(4, 0)

    def test_rectangle_dictionary(self):
        rectangle = Rectangle(10, 2, 1, 9, 12)
        expected = {
            "id": 12,
            "width": 10,
            "height": 2,
            "x": 1,
            "y": 9
        }
        self.assertEqual(rectangle.to_dictionary(), expected)


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_square_size(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_square_dictionary(self):
        square = Square(10, 2, 1, 12)
        expected = {
            "id": 12,
            "size": 10,
            "x": 2,
            "y": 1
        }
        self.assertEqual(square.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
