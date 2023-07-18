#!/usr/bin/python3
""" 0-unittest """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_int_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        self.assertEqual(b1.id, 1)

        self.assertEqual(Base().id, 2)

        b2 = Base()
        self.assertEqual(b2.id, 3)

        b3 = Base()
        self.assertEqual(b3.id, 4)

        b4 = Base(66)
        self.assertEqual(b4.id, 66)

        b5 = Base()
        self.assertEqual(b5.id, 5)

if __name__ == '__main__':
    unittest.main()
