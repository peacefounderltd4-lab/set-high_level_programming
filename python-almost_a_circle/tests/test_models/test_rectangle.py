#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset object counter before tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_rectangle_init_exists(self):
        """Test of Rectangle initialization variants exists[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)."""
        r = Rectangle(1, 2)[span_12](start_span)[span_12](end_span)
        r2 = Rectangle(1, 2, 3)[span_13](start_span)[span_13](end_span)
        r3 = Rectangle(1, 2, 3, 4)[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)
        r4 = Rectangle(1, 2, 3, 4, 5)[span_16](start_span)[span_16](end_span)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r4.id, 5)

    def test_rectangle_type_errors(self):
        """Test of Rectangle type validation errors exists[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)[span_19](start_span)[span_19](end_span)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")[span_20](start_span)[span_20](end_span)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")[span_21](start_span)[span_21](end_span)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")[span_22](start_span)[span_22](end_span)

    def test_rectangle_value_errors(self):
        """Test of Rectangle value validation errors exists[span_23](start_span)[span_23](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)[span_24](start_span)[span_24](end_span)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)[span_25](start_span)[span_25](end_span)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)[span_26](start_span)[span_26](end_span)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)[span_27](start_span)[span_27](end_span)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)[span_28](start_span)[span_28](end_span)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)[span_29](start_span)[span_29](end_span)

    def test_area_exists(self):
        """Test of area() exists[span_30](start_span)[span_30](end_span)."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str_exists(self):
        """Test of __str__() for Rectangle exists[span_31](start_span)[span_31](end_span)."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_exists(self):
        """Test of display() variants exists[span_32](start_span)[span_32](end_span)."""
        r = Rectangle(2, 2)[span_33](start_span)[span_33](end_span)
        r.display()
        r2 = Rectangle(2, 2, 1)[span_34](start_span)[span_34](end_span)
        r2.display()
        r3 = Rectangle(2, 2, 1, 1)[span_35](start_span)[span_35](end_span)
        r3.display()

    def test_to_dictionary_exists(self):
        """Test of to_dictionary() in Rectangle exists[span_36](start_span)[span_36](end_span)."""
        r = Rectangle(10, 2, 1, 9, 1)[span_37](start_span)[span_37](end_span)
        d = r.to_dictionary()[span_38](start_span)[span_38](end_span)
        self.assertIsInstance(d, dict)

    def test_update_args_exists(self):
        """Test of update() with args in Rectangle exists[span_39](start_span)[span_39](end_span)[span_40](start_span)[span_40](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)[span_41](start_span)[span_41](end_span)
        r.update()[span_42](start_span)[span_42](end_span)
        r.update(89)[span_43](start_span)[span_43](end_span)
        r.update(89, 1)[span_44](start_span)[span_44](end_span)
        r.update(89, 1, 2)[span_45](start_span)[span_45](end_span)
        r.update(89, 1, 2, 3)[span_46](start_span)[span_46](end_span)
        r.update(89, 1, 2, 3, 4)[span_47](start_span)[span_47](end_span)
        self.assertEqual(r.id, 89)

    def test_update_kwargs_exists(self):
        """Test of update() with kwargs in Rectangle exists[span_48](start_span)[span_48](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)[span_49](start_span)[span_49](end_span)
        r.update(**{'id': 89})[span_50](start_span)[span_50](end_span)
        r.update(**{'id': 89, 'width': 1})[span_51](start_span)[span_51](end_span)
        r.update(**{'id': 89, 'width': 1, 'height': 2})[span_52](start_span)[span_52](end_span)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})[span_53](start_span)[span_53](end_span)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})[span_54](start_span)[span_54](end_span)
        self.assertEqual(r.id, 89)

    def test_create_exists(self):
        """Test of Rectangle.create() exists[span_55](start_span)[span_55](end_span)."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})[span_56](start_span)[span_56](end_span)
        self.assertIsInstance(r, Rectangle)

    def test_save_to_file_exists(self):
        """Test of Rectangle.save_to_file() variants exists[span_57](start_span)[span_57](end_span)."""
        Rectangle.save_to_file(None)[span_58](start_span)[span_58](end_span)
        Rectangle.save_to_file([])[span_59](start_span)[span_59](end_span)
        Rectangle.save_to_file([Rectangle(1, 2)])[span_60](start_span)[span_60](end_span)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_exists(self):
        """Test of Rectangle.load_from_file() variants exists[span_61](start_span)[span_61](end_span)."""
        res1 = Rectangle.load_from_file()[span_62](start_span)[span_62](end_span)
        self.assertEqual(res1, [])
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        res2 = Rectangle.load_from_file()[span_63](start_span)[span_63](end_span)
        self.assertEqual(len(res2), 1)


if __name__ == "__main__":
    unittest.main()
        
