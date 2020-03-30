import unittest
from simple_calc import SimpleCalc

class TestSimpleCalc(unittest.TestCase):
    calc = SimpleCalc() # create an object
    def test_add(self):
        result = self.calc.add(2, 4)
        self.assertEqual(result, 6)
    def test_subtract(self):
        result = self.calc.subtract(4, 2)
        self.assertEqual(result, 2)
    def test_multiply(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(result, 4)
    def test_divide(self):
        result = self.calc.divide(6, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__': # this file becomes the main file (more important than the import file)
    unittest.main()