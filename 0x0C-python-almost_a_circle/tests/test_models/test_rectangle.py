#!/usr/bin/python3
''' Module for Rectangle model Unittests

Unittest classes:
    TestRectangle_init
'''
import io
import sys
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


class TestRectangle_type_bool(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, False, 3)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, False, 3)

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, False)


class TestRectangle_type_str(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 3)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "hello", 3)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, "hello", 3)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, "hello")


class TestRectangle_type_None(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None, 3)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, None, 3)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, None)


class TestRectangle_type_list(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(["apple", "banana", "cherry"], 3)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, ["apple", "banana", "cherry"], 3)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, ["apple", "banana", "cherry"], 3)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, ["apple", "banana", "cherry"])


class TestRectangle_type_dict(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"name": "John", "age": 36}, 3)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"name": "John", "age": 36}, 3)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, {"name": "John", "age": 36}, 3)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, {"name": "John", "age": 36})


class TestRectangle_type_set(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"apple", "banana", "cherry"}, 3)

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"apple", "banana", "cherry"}, 3)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, {"apple", "banana", "cherry"}, 3)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, {"apple", "banana", "cherry"})


class TestRectangle_type_frozenset(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({"apple", "banana", "cherry"}), 3)

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({"apple", "banana", "cherry"}), 3)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, frozenset({"apple", "banana", "cherry"}), 3)

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, frozenset({"apple", "banana", "cherry"}))


class TestRectangle_type_tuple(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(("apple", "banana", "cherry"), 3)

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, ("apple", "banana", "cherry"), 3)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, ("apple", "banana", "cherry"), 3)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, ("apple", "banana", "cherry"))


class TestRectangle_type_range(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(8), 3)

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(8), 3)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, range(8), 3)

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, range(8))


class TestRectangle_type_bytearray(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(5), 3)

    def test_byterray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(5), 3)

    def test_bytarray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, bytearray(5), 3)

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, bytearray(5))


class TestRectangle_type_complex(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1j, 3)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 1j, 3)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, 1j, 3)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, 1j)


class TestRectangle_type_memoryview(unittest.TestCase):
    ''' Defines wrong type tests for width, height, x and y '''
    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(bytes(5)), 3)

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(bytes(5)), 3)

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, memoryview(bytes(5)), 3)

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, memoryview(bytes(5)))


class TestRectangle_area(unittest.TestCase):
    ''' Defines tests for area of the rectangle '''
    def test_normal_area(self):
        rec1 = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(25, rec1.area())

    def test_large_area(self):
        rec1 = Rectangle(999999999, 999999999, 0, 0, 0)
        self.assertEqual((999999999 ** 2), rec1.area())

    def test_small_area(self):
        rec1 = Rectangle(2, 2, 0, 0, 0)
        self.assertEqual(4, rec1.area())

    def test_area_one_arg(self):
        rec1 = Rectangle(5, 5, 0, 0, 0)
        with self.assertRaises(TypeError):
            rec1.area(1)

    def test_area_changed_attrs(self):
        rec1 = Rectangle(2, 2, 0, 0, 0)
        rec1.width = 4
        rec1.height = 5
        self.assertEqual(20, rec1.area())


class TestRectangle_display_and_str(unittest.TestCase):
    ''' Defines tests for displaying of the rectangle '''
    @staticmethod
    def capture_stdout(rec, method):
        ''' Captures and prints to stdout
            Args:
                rec(Rectangle): Rectangle to print to stdout
                method(str): method to run on rect
            Return: printed rectangle
        '''
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return capture

# display tests
    def test_display_width_height(self):
        rec1 = Rectangle(5, 3, 0, 0, 0)
        capture = TestRectangle_display_and_str.capture_stdout(rec1, "display")
        self.assertEqual("#####\n#####\n#####\n", capture.getvalue())

    def test_display_width_height_x(self):
        rec1 = Rectangle(5, 3, 1, 0, 1)
        capture = TestRectangle_display_and_str.capture_stdout(rec1, "display")
        self.assertEqual(" #####\n #####\n #####\n", capture.getvalue())

    def test_display_width_height_y(self):
        rec1 = Rectangle(5, 3, 0, 1, 0)
        capture = TestRectangle_display_and_str.capture_stdout(rec1, "display")
        self.assertEqual("\n#####\n#####\n#####\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        rec1 = Rectangle(5, 3, 2, 1, 0)
        capture = TestRectangle_display_and_str.capture_stdout(rec1, "display")
        self.assertEqual("\n  #####\n  #####\n  #####\n", capture.getvalue())

    def test_display_one_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 0)
        with self.assertRaises(TypeError):
            rec1.display(1)

# __str__ tests

    def test_str_method_one_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 0)
        with self.assertRaises(TypeError):
            rec1.__str__(1)

    def test_str_width_height(self):
        rec1 = Rectangle(5, 3, 0, 0, 0)
        capture = TestRectangle_display_and_str.capture_stdout(rec1, "print")
        answer = "[Rectangle] ({}) 0/0 - 5/3\n".format(rec1.id)
        self.assertEqual(answer, capture.getvalue())

    def test_str_width_height_x(self):
        rec1 = Rectangle(5, 3, 1, 0, 0)
        answer = "[Rectangle] ({}) 1/0 - 5/3".format(rec1.id)
        self.assertEqual(answer, rec1.__str__())

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


class TestRectangle_update_args(unittest.TestCase):
    ''' Unittests for testing update args of the Rectangle class '''

    def test_update_args_zero(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update()
        self.assertEqual("[Rectangle] (2) 2/1 - 5/3", str(rec1))

    def test_update_one_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1)
        self.assertEqual("[Rectangle] (1) 2/1 - 5/3", str(rec1))

    def test_update_two_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1, 8)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/3", str(rec1))

    def test_update_three_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1, 8, 7)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/7", str(rec1))

    def test_update_four_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1, 8, 7, 5)
        self.assertEqual("[Rectangle] (1) 5/1 - 8/7", str(rec1))

    def test_update_five_arg(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1, 8, 7, 5, 6)
        self.assertEqual("[Rectangle] (1) 5/6 - 8/7", str(rec1))

    def test_update_more_than_five_args(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(1, 8, 7, 5, 6, 4)
        self.assertEqual("[Rectangle] (1) 5/6 - 8/7", str(rec1))

    def test_update_args_None(self):
        rec1 = Rectangle(5, 3, 2, 1, 2)
        rec1.update(None)
        answer = "[Rectangle] ({}) 2/1 - 5/3".format(rec1.id)

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
