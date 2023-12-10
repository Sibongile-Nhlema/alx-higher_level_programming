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
        sq1 = Square(5, 3, 2, 1)
        with self.assertRaises(TypeError):
            sq1.__str__(5)

    def test_str_size(self):
        sq1 = Square(5)
        capture = TestSquare_display_and_str.capture_stdout(sq1, "print")
        answer = "[Square] ({}) 0/0 - 5\n".format(sq1.id)
        self.assertEqual(answer, capture.getvalue())

    def test_str_size_x(self):
        sq1 = Square(3, 3)
        answer = "[Square] ({}) 3/0 - 3".format(sq1.id)
        self.assertEqual(answer, str(sq1))

    def test_str_size_x_y(self):
        sq1 = Square(3, 3, 5)
        answer = "[Square] ({}) 3/5 - 3".format(sq1.id)
        self.assertEqual(answer, str(sq1))

    def test_str_size_x_y_id(self):
        sq1 = Square(3, 3, 5, 7)
        answer = "[Square] (7) 3/5 - 3".format(sq1.id)
        self.assertEqual(answer, str(sq1))

    def test_str_changed_attributes(self):
        sq1 = Square(5, 3, 1, [4])
        sq1.width = 10
        sq1.height = 2
        sq1.x = 4
        sq1.y = 7
        self.assertEqual("[Square] ([4]) 4/7 - 2", str(sq1))

class TestSquare_getters_setters(unittest.TestCase):
    ''' Defines getter and setter test cases for the square class '''
    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 4, 6).size)

    def test_size_setter(self):
        sq1 = Square(1, 2, 3, 4)
        sq1.size = 8
        self.assertEqual(8, sq1.size)

    def test_width_getter(self):
        sq1 = Square(1, 2, 3, 4)
        sq1.size = 8
        self.assertEqual(8, sq1.width)

    def test_height_getter(self):
        sq1 = Square(4, 1, 9, 2)
        sq1.size = 8
        self.assertEqual(8, sq1.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(3).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(6).y)

class TestSquare_update_args(unittest.TestCase):
    ''' Unittests for testing update args of the Rectangle class '''

    def test_update_args_zero(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update()
        self.assertEqual("[Square] (2) 2/1 - 5/3", str(sq1))

    def test_update_one_arg(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1)
        self.assertEqual("[Square] (1) 2/1 - 5/3", str(sq1))

    def test_update_two_arg(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1, 8)
        self.assertEqual("[Square] (1) 2/1 - 8/3", str(sq1))

    def test_update_three_arg(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1, 8, 7)
        self.assertEqual("[Square] (1) 2/1 - 8/7", str(sq1))

    def test_update_four_arg(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1, 8, 7, 5)
        self.assertEqual("[Square] (1) 5/1 - 8/7", str(sq1))

    def test_update_five_arg(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1, 8, 7, 5, 6)
        self.assertEqual("[Square] (1) 5/6 - 8/7", str(sq1))

    def test_update_more_than_five_args(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(1, 8, 7, 5, 6, 4)
        self.assertEqual("[Square] (1) 5/6 - 8/7", str(sq1))

    def test_update_args_None(self):
        sq1 = Square(5, 3, 2, 1, 2)
        sq1.update(None)
        answer = "[Rectangle] ({}) 2/1 - 5/3".format(sq1.id)

    def test_update_args_None_id_and_other_args(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(None, 7, 5, 6, 4)
        answer = "[Rectangle] ({}) 6/4 - 7/5".format(rec1.id)
        self.assertEqual(answer, str(rec1))

    def test_update_args_twice(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(89, 2, 3, 4, 5, 6)
        rec1.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rec1))

class TestRectangle_update_kwargs(unittest.TestCase):
    '''Unittests for update kwargs method '''

    def test_update_one_kwarg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(id=1)
        self.assertEqual("[Rectangle] (1) 2/1 - 5/3", str(rec1))

    def test_update_two_kwarg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(id=1, width=8)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/3", str(rec1))

    def test_update_three_kwarg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(height=7, id=1, width=8)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/7", str(rec1))

    def test_update_four_kwarg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(x=5, id=1, width=8, height=7)
        self.assertEqual("[Rectangle] (1) 5/1 - 8/7", str(rec1))

    def test_update_five_kwarg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(y=6, id=1, width=8, x=5, height=7)
        self.assertEqual("[Rectangle] (1) 5/6 - 8/7", str(rec1))

    def test_update_kwargs_None(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(id=None)
        answer = "[Rectangle] ({}) 2/1 - 5/3".format(rec1.id)

    def test_update_kwargs_None_id_and_other_kwargs(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(id=None, width=8, x=5, height=7, y=6)
        answer = "[Rectangle] ({}) 5/6 - 8/7".format(rec1.id)
        self.assertEqual(answer, str(rec1))

    def test_update_kwargs_twice(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(id=89, x=1, height=2)
        rec1.update(id=6, width=5, height=4, x=3, y=2)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rec1))


if __name__ == "__main__":
    unittest.main()
