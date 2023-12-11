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
            Square(2, 6, 3, 3, 4, 3)


class TestSquare_type_float(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_float_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.6)


class TestSquare_type_bool(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_bool_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False)


class TestSquare_type_str(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_str_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("bye")


class TestSquare_type_None(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_None_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)


class TestSquare_type_list(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_list_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(["apple", "bandjo", "cherry"])


class TestSquare_type_dict(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_dict_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"name": "Johnny", "age": 6})


class TestSquare_type_set(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_set_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"apple", "banana", "edges"})


class TestSquare_type_frozenset(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_frozenset_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({"apple", "blue", "cherry"}))


class TestSquare_type_tuple(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_tuple_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(("red", "orange", "yellow"))


class TestSquare_type_range(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_range_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(8))


class TestSquare_type_bytearray(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_bytearray_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(5))


class TestSquare_type_complex(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_complex_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1j)


class TestSquare_type_memoryview(unittest.TestCase):
    ''' Defines wrong type tests for side '''
    def test_memoryview_side(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(bytes(5)))


class TestSquare_area(unittest.TestCase):
    ''' Defines tests for area of the square '''
    def test_normal_area(self):
        sq1 = Square(3)
        self.assertEqual(9, sq1.area())

    def test_large_area(self):
        sq1 = Square(999999999)
        self.assertEqual((999999999 ** 2), sq1.area())

    def test_small_area(self):
        sq1 = Square(2)
        self.assertEqual(4, sq1.area())

    def test_area_one_arg(self):
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.area(1)

    def test_area_changed_side(self):
        sq1 = Square(3)
        sq1.side = 9
        self.assertEqual(9, sq1.area())


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
        sq1 = Square(5, 2, 1, 2)
        sq1.update()
        self.assertEqual("[Square] (2) 2/1 - 5", str(sq1))

    def test_update_one_arg(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(1)
        self.assertEqual("[Square] (1) 2/1 - 5", str(sq1))

    def test_update_two_arg(self):
        sq1 = Square(5, 3, 1, 2)
        sq1.update(1, 8)
        self.assertEqual("[Square] (1) 3/1 - 8", str(sq1))

    def test_update_three_arg(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(1, 8, 7)
        self.assertEqual("[Square] (1) 7/1 - 8", str(sq1))

    def test_update_four_arg(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(1, 8, 7, 5)
        self.assertEqual("[Square] (1) 7/5 - 8", str(sq1))

    def test_update_five_arg(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(1, 8, 7, 5, 6)
        self.assertEqual("[Square] (1) 7/5 - 8", str(sq1))

    def test_update_more_than_five_args(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(1, 8, 7, 5, 6, 4)
        self.assertEqual("[Square] (1) 7/5 - 8", str(sq1))

    def test_update_args_None(self):
        sq1 = Square(5, 2, 1, 2)
        sq1.update(None)
        answer = "[Rectangle] ({}) 2/1 - 5/3".format(sq1.id)

    def test_update_args_None_id_and_other_args(self):
        rec1 = Rectangle(5, 2, 1, 2)
        rec1.update(None, 7, 5, 6, 4)
        answer = "[Rectangle] ({}) 6/4 - 7/5".format(rec1.id)
        self.assertEqual(answer, str(rec1))

    def test_update_args_twice(self):
        rec1 = Rectangle(5, 2, 1, 2)
        rec1.update(89, 3, 4, 5, 6)
        rec1.update(6, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 2/89 - 4/3", str(rec1))


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


class TestSquareToDictionary(unittest.TestCase):
    ''' testing the to_dictionary method '''

    def test_to_dictionary_with_correct_output(self):
        square = Square(15, 4, 2, 5)
        expected_output = {'id': 5, 'x': 4, 'size': 15, 'y': 2}
        self.assertDictEqual(expected_output, square.to_dictionary())

    def test_to_dictionary_with_no_object_changes(self):
        square1 = Square(15, 3, 2, 7)
        square2 = Square(5, 3, 15)
        square2.update(**square1.to_dictionary())
        self.assertNotEqual(square1, square2)

    def test_to_dictionary_with_invalid_argument(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            square.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
