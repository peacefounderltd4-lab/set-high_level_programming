#!/usr/bin/python3
"""Unit tests for Rectangle."""
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(
            str(rect),
            "[Rectangle] (12) 2/1 - 4/6"
        )

    def test_width_type(self):
        with self.assertRaisesRegex(
            TypeError, "width must be an integer"
        ):
            Rectangle("4", 2)

    def test_width_value(self):
        with self.assertRaisesRegex(
            ValueError, "width must be > 0"
        ):
            Rectangle(0, 2)

    def test_height_type(self):
        with self.assertRaisesRegex(
            TypeError, "height must be an integer"
        ):
            Rectangle(4, "2")

    def test_height_value(self):
        with self.assertRaisesRegex(
            ValueError, "height must be > 0"
        ):
            Rectangle(4, 0)

    def test_x_type(self):
        with self.assertRaisesRegex(
            TypeError, "x must be an integer"
        ):
            Rectangle(4, 2, "1")

    def test_x_value(self):
        with self.assertRaisesRegex(
            ValueError, "x must be >= 0"
        ):
            Rectangle(4, 2, -1)

    def test_y_type(self):
        with self.assertRaisesRegex(
            TypeError, "y must be an integer"
        ):
            Rectangle(4, 2, 0, "1")

    def test_y_value(self):
        with self.assertRaisesRegex(
            ValueError, "y must be >= 0"
        ):
            Rectangle(4, 2, 0, -1)

    def test_update_args(self):
        rect = Rectangle(1, 1)
        rect.update(89, 2, 3, 4, 5)

        self.assertEqual(
            str(rect),
            "[Rectangle] (89) 4/5 - 2/3"
        )

    def test_update_kwargs(self):
        rect = Rectangle(1, 1)
        rect.update(width=4, height=5, x=2, y=3)

        self.assertEqual(
            str(rect),
            "[Rectangle] ({}) 2/3 - 4/5".format(rect.id)
        )

    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9, 7)

        self.assertEqual(
            rect.to_dictionary(),
            {
                "id": 7,
                "width": 10,
                "height": 2,
                "x": 1,
                "y": 9
            }
        )


if __name__ == "__main__":
    unittest.main()
