#!/usr/bin/python3
''' Module for Rectangle model Unittests

Unittest classes:
    TestRectangle_init
'''
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_args(unittest.TestCase):
    ''' Defines argument test cases for the rectangle class '''
    def test_two_args(self):
        rec1 = Rectangle(2, 4)
        rec2 = Rectangle(5, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_three_args(self):
        rec1 = Rectangle(2, 4, 3)
        rec2 = Rectangle(5, 10, 7)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_four_args(self):
        rec1 = Rectangle(2, 4, 3, 5)
        rec2 = Rectangle(5, 10, 7, 5)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_five_args(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        self.assertEqual(4, rec1.id)

    def test_class_type(self):
        self.assertIsInstance(Rectangle(3, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3, 5, 4, 3)

class TestRectangle_private_args(unittest.TestCase):
    ''' Defines private instance test cases for the rectangle class '''
    def test_width_p_status(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 7, 8, 2, 4).__width)

    def test_height_p_status(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 7, 8, 2, 4).__height)

    def test_x_p_status(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 7, 8, 2, 4).__x)

    def test_y_p_status(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 7, 8, 2, 4).__y)

class TestRectangle_setters(unittest.TestCase):
    ''' Defines setter test cases for the rectangle class '''
    def test_setter_for_width(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        rec1.width = 5
        self.assertEqual(5, rec1.width)

    def test_setter_for_height(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        rec1.height = 5
        self.assertEqual(5, rec1.height)

    def test_setter_for_x(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        rec1.x = 5
        self.assertEqual(5, rec1.x)

    def test_setter_for_y(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        rec1.y = 7
        self.assertEqual(7, rec1.y)

class TestRectangle_getters(unittest.TestCase):
    ''' Defines getter test cases for the rectangle class '''
    def test_getter_for_width(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        self.assertEqual(2, rec1.width)

    def test_getter_for_height(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        self.assertEqual(4, rec1.height)

    def test_getter_for_x(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        self.assertEqual(3, rec1.x)

    def test_getter_for_y(self):
        rec1 = Rectangle(2, 4, 3, 5, 4)
        self.assertEqual(5, rec1.y)

class TestRectangle_type_float(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(7.5, 3)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 7.5, 3)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, 7.5, 3)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, 7.5)


if __name__ == "__main__":
    unittest.main()
