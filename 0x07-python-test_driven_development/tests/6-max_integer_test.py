#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_docmodule_string(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)
    
    def test_docfunction_string(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_Big_numbers(self):
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer(), None)

    def test_instences(self):
        with self.assertRaises(TypeError):
            max_integer({6, 0, 0, 0, 9})
        with self.assertRaises(TypeError):
            max_integer({6, 9}, {6, 0, 9})
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer([-60, 6.9, "str", {6, 9}])

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_mix_ints_floats(self):
        self.assertEqual(max_integer([{1, 9}, {2}, {3}]), {1, 9})
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, -10, 10]), 10)

    def test_strings_lists(self):
        self.assertEqual(max_integer(['q', 'w', 'e', 'r', 't', 'y']), 'y')
        self.assertEqual(max_integer("abcxyz"), 'z')
        self.assertEqual(max_integer(["sdfaf", 'w']), 'w')
        self.assertEqual(max_integer("abcxyz"), 'z')

    if __name__ == "__main__":
        unittest.main()
