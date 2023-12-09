#!/usr/bin/python3
''' Module for Rectangle model Unittests

Unittest classes:
    TestRectangle_args
'''
import io
import sys
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_args(unittest.TestCase):
    ''' Defines argument test cases for the square class '''
    def test_two_args(self):
        sq1 = Square(2, 4)
        sq2 = Square(5, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three_args(self):
        sq1 = Square(2, 4, 3)
        sq2 = Square(5, 10, 7)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four_args(self):
        sq2 = Square(5, 10, 7, 5)
        self.assertEqual(5, sq2.id)

    def test_five_args(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, 4, 3, 5, 4)

    def test_class_type(self):
        self.assertIsInstance(Square(3, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        sq1 = Square(7)
        sq2 = Square(8)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(2, 4, 3, 5, 4, 3)

class TestSquare_display_and_str(unittest.TestCase):
    ''' Defines tests for displaying of the square '''
    @staticmethod
    def capture_stdout(sq, method):
        ''' Captures and prints to stdout
            Args:
                sq(Square): Square to print to stdout
                method(str): method to run on rect
            Return: printed square
        '''
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

# __str__ tests
    def test_str_method_one_arg(self):
        sq1 = Square(5, 3, 2, 1, 0)
        with self.assertRaises(TypeError):
            sq1.__str__(5)

    def test_str_size(self):
        sq1 = Square(5)
        capture = TestSquare_display_and_str.capture_stdout(sq1, "print")
        answer = "[Square] ({}) 0/0 - 5\n".format(sq1.id)
        self.assertEqual(answer, capture.getvalue())

    def test_str_width_height_x_y(self):
        rec1 = Rectangle(5, 3, 1, 2, 0)
        answer = "[Rectangle] ({}) 1/2 - 5/3".format(rec1.id)
        self.assertEqual(answer, str(rec1))

    def test_str_width_height_x_y_id(self):
        rec1 = Rectangle(5, 3, 1, 2, 4)
        self.assertEqual("[Rectangle] (4) 1/2 - 5/3", str(rec1))

    def test_str_changed_attributes(self):
        rec1 = Rectangle(5, 3, 1, 2, [4])
        rec1.width = 10
        rec1.height = 2
        rec1.x = 4
        rec1.y = 7
        self.assertEqual("[Rectangle] ([4]) 4/7 - 10/2", str(rec1))


if __name__ == "__main__":
    unittest.main()
