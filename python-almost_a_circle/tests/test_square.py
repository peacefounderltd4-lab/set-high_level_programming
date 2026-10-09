#!/usr/bin/python3
"""Unit tests for Square."""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        square = Square(5, 2, 1, 10)

        self.assertEqual(
            str(square),
            "[Square] (10) 2/1 - 5"
        )

    def test_size_setter(self):
        square = Square(5)
        square.size = 10

        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_size_type(self):
        square = Square(5)

        with self.assertRaisesRegex(
            TypeError, "width must be an integer"
        ):
            square.size = "9"

    def test_update_args(self):
        square = Square(5)
        square.update(1, 2, 3, 4)

        self.assertEqual(
            str(square),
            "[Square] (1) 3/4 - 2"
        )

    def test_update_kwargs(self):
        square = Square(5)
        square.update(size=7, x=2, y=1, id=89)

        self.assertEqual(
            str(square),
            "[Square] (89) 2/1 - 7"
        )

    def test_to_dictionary(self):
        square = Square(10, 2, 1, 8)

        self.assertEqual(
            square.to_dictionary(),
            {
                "id": 8,
                "size": 10,
                "x": 2,
                "y": 1
            }
        )


if __name__ == "__main__":
    unittest.main()
