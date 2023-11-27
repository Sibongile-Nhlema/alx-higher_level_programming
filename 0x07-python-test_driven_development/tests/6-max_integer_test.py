#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        ''' 
        Test with an empty list
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([]), None)

    def test_all_negative_numbers(self):
        '''
        Test with all negative values
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([-46, -3, -1, -9, -5]), -1)

    def test_all_same_number(self):
        '''
        Test with values all the same
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-4, -4, -4]), -4)

    def test_both_negative_and_positive_numbers(self):
        '''
        Test with both negative and positive numbers
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([2, 0, -2]), 2)
        self.assertEqual(max_integer([0, -9, -2]), 0)

    def test_multiple_max_numbers(self):
        '''
        Tests with multiple values of the same number being max
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([12, 9, 0, -4, 12, 12]), 12)

    def test_multiple_not_numbers(self):
        '''
        Tests with multiple values of the same number being not max
        Args:
            self: Argument
        '''
        self.assertEqual(max_integer([12, 9, 100, -4, 12, 12]), 100)

    def test_extremely_large_number(self):
        '''
        Test with a very large number
        Args:
            self: Argument
        '''
        large_number = [1, 2, 4, 6, 67, 24, 90, 322, 455, 768, 1000, 4,
                6, 67, 800, 234, 567, 788, 334, 234, 11, 222, 765, 975,
                334, 567, 322, 455, 768, 34, 65, 345, 76, 235, 768, 23,
                879, 43, 79, 453 ,43, 435, 908, 43, 356, 68, 766]
        self.assertEqual(max_integer(large_number), 1000)

if __name__ == '__main__':
    unittest.main()
