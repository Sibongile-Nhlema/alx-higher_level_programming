#!/usr/bin/python3
''' Module for Base model Unittests '''
import unittest
from models.base import Base


class ModelBaseTest(unittest.TestCase):
    ''' Defines test cases for the base class '''
    def test_id_given(self):
        self.assertEqual(base(35).id, 35)

if __name__ == "__main__":
    unittest.main()
