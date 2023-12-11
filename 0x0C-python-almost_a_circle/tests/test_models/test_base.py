#!/usr/bin/python3
''' Module for Base model Unittests

Unittest classes:
    TestBase_init
'''
import os
import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    ''' Defines test cases for the base class '''

#  no id's given
    def test_id_not_given(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_not_given_multiple(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)

    def test_id_is_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

#  id's given
    def test_id_given(self):
        b1 = Base(20)
        self.assertEqual(b1.id, 20)

    def test_id_multiple(self):
        with self.assertRaises(TypeError):
            Base(6, 4)

    def test_id_infinity(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_neg_infinity(self):
        self.assertEqual(float('-inf'), Base(float('-inf')).id)

# mix of no id and id given
    def test_nb_instances_after_id_given(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        b4 = Base(76)
        b5 = Base()
        b6 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 76)
        self.assertEqual(b5.id, b2.id + 1)
        self.assertEqual(b6.id, b5.id + 1)

#  test whether id is public
    def test_id_is_public(self):
        b1 = Base(8)
        b1.id = 90
        self.assertEqual(90, b1.id)

# test whether nb_instances is private
    def test_nb_instances_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(23).__nb_instances)

# cases that should raise errors, unlikely cases where id is not an int
    def test_id_Nan(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

# test id is not type int
    def test_id_float(self):
        self.assertEqual(2.5, Base(2.5).id)

    def test_id_str(self):
        self.assertEqual('string', Base('string').id)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_set(self):
        self.assertEqual({"apple", "banana", "cherry"},
                         Base({"apple", "banana", "cherry"}).id)

    def test_id_frozenset(self):
        self.assertEqual(frozenset({"apple", "banana", "cherry"}),
                         Base(frozenset({"apple", "banana", "cherry"})).id)

    def test_id_list(self):
        self.assertEqual(["list", "list", "list"],
                         Base(["list", "list", "list"]).id)

    def test_id_tuple(self):
        self.assertEqual(("list", "list", "list"),
                         Base(("list", "list", "list")).id)

    def test_id_dict(self):
        self.assertEqual({"name": "John", "age": 36},
                         Base({"name": "John", "age": 36}).id)

    def test_id_range(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_id_complex(self):
        self.assertEqual(1j, Base(1j).id)

    def test_id_bytes(self):
        self.assertEqual(b"Hello", Base(b"Hello").id)

    def test_id_bytearray(self):
        self.assertEqual(bytearray(5), Base(bytearray(5)).id)

    def test_id_memoryview(self):
        self.assertEqual(memoryview(bytes(10)), Base(memoryview(bytes(10))).id)


class TestBase_to_json_string(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_to_json_string_rectangle(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_type_rectangle(self):
        rec1 = Rectangle(3, 5, 7, 9, 11)
        self.assertEqual(str, type(Base.to_json_string([rec1.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)


class TestBase_to_json_string_square(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_type_square(self):
        s = Square(5, 20, 15, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)


if __name__ == "__main__":
    unittest.main()
