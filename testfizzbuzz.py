import unittest
import fizzbuzz

class TestMultiples(unittest.TestCase):
    def testThree(self):
        self.assertEqual(fizzbuzz.testThree, ("1\n2\nFizz"))