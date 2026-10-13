
#!/usr/bin/python3
"""Unit tests for the Almost a Circle models."""

import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base methods."""

    def test_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        data = [{"id": 1}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_square_csv_round_trip(self):
        squares = [Square(5, 2, 3, 44), Square(7, 1, 0, 45)]
        Square.save_to_file_csv(squares)
        loaded = Square.load_from_file_csv()

        self.assertEqual(
            [item.to_dictionary() for item in loaded],
            [item.to_dictionary() for item in squares],
        )
        os.remove("Square.csv")

    def test_rectangle_json_round_trip(self):
        rectangle = Rectangle(3, 4, 1, 2, 77)
        Rectangle.save_to_file([rectangle])
        loaded = Rectangle.load_from_file()

        self.assertEqual(
            loaded[0].to_dictionary(), rectangle.to_dictionary()
        )
        os.remove("Rectangle.json")


class TestRectangle(unittest.TestCase):
    """Test Rectangle methods."""

    def test_area_and_string(self):
        rectangle = Rectangle(4, 5, 2, 1, 12)
        self.assertEqual(rectangle.area(), 20)
        self.assertEqual(
            str(rectangle), "[Rectangle] (12) 2/1 - 4/5"
        )

    def test_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("4", 5)
        with self.assertRaises(ValueError):
            Rectangle(4, 0)
        with self.assertRaises(ValueError):
            Rectangle(4, 5, -1, 0)


class TestSquare(unittest.TestCase):
    """Test Square methods."""

    def test_size_and_string(self):
        square = Square(5, 2, 1, 20)
        self.assertEqual(square.area(), 25)
        self.assertEqual(str(square), "[Square] (20) 2/1 - 5")

    def test_dictionary(self):
        square = Square(3, 1, 2, 10)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 10, "size": 3, "x": 1, "y": 2},
        )


if __name__ == "__main__":
    unittest.main()
    
