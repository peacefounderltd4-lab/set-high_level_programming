#!/usr/bin/python3
"""Test Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle."""

    def test_create(self):
        """Test creation."""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id(self):
        """Test ID."""
        r = Rectangle(1, 2, id=89)
        self.assertEqual(r.id, 89)

    def test_invalid_width_type(self):
        """Test width type."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_invalid_height_type(self):
        """Test height type."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_invalid_width_value(self):
        """Test width value."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_invalid_height_value(self):
        """Test height value."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_invalid_x_type(self):
        """Test x type."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "x")

    def test_invalid_y_type(self):
        """Test y type."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "y")

    def test_invalid_x_value(self):
        """Test x value."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_invalid_y_value(self):
        """Test y value."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        """Test string."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test positional update."""
        r = Rectangle(10, 10)
        r.update(89, 2, 3, 4, 5)

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test keyword update."""
        r = Rectangle(10, 10)
        r.update(width=2, height=3, x=4, y=5, id=89)

        self.assertEqual(r.to_dictionary(), {
            "id": 89,
            "width": 2,
            "height": 3,
            "x": 4,
            "y": 5
        })

    def test_to_dictionary(self):
        """Test dictionary."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {
            "id": 1,
            "width": 10,
            "height": 2,
            "x": 1,
            "y": 9
        })


if __name__ == "__main__":
    unittest.main()
