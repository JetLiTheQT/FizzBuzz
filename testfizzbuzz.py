import unittest
import fizzbuzz

class TestMultiples(unittest.TestCase):
    def testThree(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")
    def testFive(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(50), "Buzz")
