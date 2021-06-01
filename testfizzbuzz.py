import unittest
import fizzbuzz

class TestMultiples(unittest.TestCase):
    def testThree(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")