#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def tearDown(self):
        """Clean up created files after tests."""
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_create_square(self):
        """Test of Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3 }) exists."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) exists."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) exists."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_squares(self):
        """Test of Square.save_to_file([Square(1)]) exists."""
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertIn("size", f.read())

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn't exist exists."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        res = Square.load_from_file()
        self.assertEqual(res, [])

    def test_load_from_file_exists(self):
        """Test of Square.load_from_file() when file exists exists."""
        s = Square(5, 1, 2, 89)
        Square.save_to_file([s])
        list_squares = Square.load_from_file()
        self.assertEqual(len(list_squares), 1)
        self.assertEqual(list_squares[0].id, 89)
        self.assertEqual(list_squares[0].size, 5)


if __name__ == "__main__":
    unittest.main()
            
