#!/usr/bin/python3
''' Module for Rectangle model Unittests

Unittest classes:
    TestRectangle_init
'''
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class ModelRectangleTest(unittest.TestCase):
    ''' Defines test cases for the base class '''
# ALL SHOULD PASS
# correct number of args
    def test_two_args(self):
        rec1 = Rectangle(2, 4)
        rec2 = Rectangle(5, 10)
        self.assertEqual(rec1.id, rec2.id - 1)
# check if Rectangle inherited Base
# check if nb_instance is correct with Rectange
# check if id is correct within Rectangle
# try int as input

# ALL SHOULD FAIL AND/OR RAISE ERRORS
# no args
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
# only one args
    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7)
# try float as input
# try double as input
# try max as input
# try min as input
# try infinity as input
# try NaN as input
# try str as input
# try dict as input
# try list as input
# try set as input


if __name__ == "__main__":
    unittest.main()
