#!/usr/bin/python3
"""Test Square class."""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square."""

    def test_create(self):
        """Test creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_id(self):
        """Test ID."""
        s = Square(5, id=89)
        self.assertEqual(s.id, 89)

    def test_area(self):
        """Test area."""
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        """Test string."""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_invalid_size(self):
        """Test invalid size."""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.size = "10"

        with self.assertRaises(ValueError):
            s.size = 0

    def test_update_args(self):
        """Test positional update."""
        s = Square(5)
        s.update(10, 2, 3, 4)

        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test keyword update."""
        s = Square(5)
        s.update(size=7, x=2, y=3, id=89)

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """Test dictionary."""
        s = Square(10, 2, 1, 1)

        self.assertEqual(s.to_dictionary(), {
            "id": 1,
            "size": 10,
            "x": 2,
            "y": 1
        })


if __name__ == "__main__":
    unittest.main()
