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
    def testFiveandThree(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(60), "FizzBuzz")
    
