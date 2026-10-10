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
        """Clean up generated files after tests."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_rectangle_init_1_2(self):
        """Test of Rectangle(1, 2) exists[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span)."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_init_1_2_3(self):
        """Test of Rectangle(1, 2, 3) exists[span_15](start_span)[span_15](end_span)[span_16](start_span)[span_16](end_span)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_init_1_2_3_4(self):
        """Test of Rectangle(1, 2, 3, 4) exists[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_init_1_2_3_4_5(self):
        """Test of Rectangle(1, 2, 3, 4, 5) exists[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_type_str_1(self):
        """Test of Rectangle("1", 2) exists[span_21](start_span)[span_21](end_span)[span_22](start_span)[span_22](end_span)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_type_str_2(self):
        """Test of Rectangle(1, "2") exists[span_23](start_span)[span_23](end_span)[span_24](start_span)[span_24](end_span)."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_type_str_3(self):
        """Test of Rectangle(1, 2, "3") exists[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_type_str_4(self):
        """Test of Rectangle(1, 2, 3, "4") exists[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span)."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_value_neg_width(self):
        """Test of Rectangle(-1, 2) exists[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_value_neg_height(self):
        """Test of Rectangle(1, -2) exists[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_value_zero_width(self):
        """Test of Rectangle(0, 2) exists[span_33](start_span)[span_33](end_span)[span_34](start_span)[span_34](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_value_zero_height(self):
        """Test of Rectangle(1, 0) exists[span_35](start_span)[span_35](end_span)[span_36](start_span)[span_36](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_value_neg_x(self):
        """Test of Rectangle(1, 2, -3) exists[span_37](start_span)[span_37](end_span)[span_38](start_span)[span_38](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_value_neg_y(self):
        """Test of Rectangle(1, 2, 3, -4) exists[span_39](start_span)[span_39](end_span)[span_40](start_span)[span_40](end_span)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test of area() exists[span_41](start_span)[span_41](end_span)[span_42](start_span)[span_42](end_span)."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test of __str__() for Rectangle exists[span_43](start_span)[span_43](end_span)[span_44](start_span)[span_44](end_span)."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        """Test of display() without x and y exists[span_45](start_span)[span_45](end_span)[span_46](start_span)[span_46](end_span)."""
        r = Rectangle(2, 2)
        r.display()

    def test_display_no_y(self):
        """Test of display() without y exists[span_47](start_span)[span_47](end_span)[span_48](start_span)[span_48](end_span)."""
        r = Rectangle(2, 2, 1)
        r.display()

    def test_display(self):
        """Test of display() exists[span_49](start_span)[span_49](end_span)[span_50](start_span)[span_50](end_span)[span_51](start_span)[span_51](end_span)."""
        r = Rectangle(2, 2, 1, 1)
        r.display()

    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle exists[span_52](start_span)[span_52](end_span)[span_53](start_span)[span_53](end_span)[span_54](start_span)[span_54](end_span)."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_update_empty(self):
        """Test of update() in Rectangle exists[span_55](start_span)[span_55](end_span)[span_56](start_span)[span_56](end_span)[span_57](start_span)[span_57](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(r.id, 10)

    def test_update_89(self):
        """Test of update(89) in Rectangle exists[span_58](start_span)[span_58](end_span)[span_59](start_span)[span_59](end_span)[span_60](start_span)[span_60](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test of update(89, 1) in Rectangle exists[span_61](start_span)[span_61](end_span)[span_62](start_span)[span_62](end_span)[span_63](start_span)[span_63](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        """Test of update(89, 1, 2) in Rectangle exists[span_64](start_span)[span_64](end_span)[span_65](start_span)[span_65](end_span)[span_66](start_span)[span_66](end_span)[span_67](start_span)[span_67](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Rectangle exists[span_68](start_span)[span_68](end_span)[span_69](start_span)[span_69](end_span)[span_70](start_span)[span_70](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        """Test of update(89, 1, 2, 3, 4) in Rectangle exists[span_71](start_span)[span_71](end_span)[span_72](start_span)[span_72](end_span)[span_73](start_span)[span_73](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        """Test of update(**{ 'id': 89 }) in Rectangle exists[span_74](start_span)[span_74](end_span)[span_75](start_span)[span_75](end_span)[span_76](start_span)[span_76](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_width(self):
        """Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle exists[span_77](start_span)[span_77](end_span)[span_78](start_span)[span_78](end_span)[span_79](start_span)[span_79](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_height(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists[span_80](start_span)[span_80](end_span)[span_81](start_span)[span_81](end_span)[span_82](start_span)[span_82](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_x(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists[span_83](start_span)[span_83](end_span)[span_84](start_span)[span_84](end_span)[span_85](start_span)[span_85](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_y(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists[span_86](start_span)[span_86](end_span)[span_87](start_span)[span_87](end_span)[span_88](start_span)[span_88](end_span)."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists[span_89](start_span)[span_89](end_span)[span_90](start_span)[span_90](end_span)."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertIsInstance(r, Rectangle)

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None) in Rectangle exists[span_91](start_span)[span_91](end_span)[span_92](start_span)[span_92](end_span)."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([]) in Rectangle exists[span_93](start_span)[span_93](end_span)[span_94](start_span)[span_94](end_span)."""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_rects(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists[span_95](start_span)[span_95](end_span)[span_96](start_span)[span_96](end_span)."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn't exist exists[span_97](start_span)[span_97](end_span)[span_98](start_span)[span_98](end_span)."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        res = Rectangle.load_from_file()
        self.assertEqual(res, [])

    def test_load_from_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists exists[span_99](start_span)[span_99](end_span)[span_100](start_span)[span_100](end_span)."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        res = Rectangle.load_from_file()
        self.assertEqual(len(res), 1)


if __name__ == "__main__":
    unittest.main()
        
