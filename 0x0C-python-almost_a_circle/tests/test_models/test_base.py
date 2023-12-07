#!/usr/bin/python3
''' Module for Base model Unittests

Unittest classes:
    TestBase_init
'''
import os
import unittest
from models.base import Base


class ModelBaseTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
