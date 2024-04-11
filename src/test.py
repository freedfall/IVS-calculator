## 
# @file test.py
# @brief Test cases for the math library
# @Author: Timur Kininbayev
# @Author: Artem Dvorychanskiy
#
##

#Imports
import unittest
from src import calc

#Functions
class TestMathLibrary(unittest.TestCase):

    def test_addition(self):
        result = add(1, 2)
        self.assertEqual(result, 3)
    
    def test_addition_of_negative_numbers(self):
        result = add(-1, -2)
        self.assertEqual(result, -3)
    
    def test_addition_of_positive_and_negative_numbers(self):
        result = add(-1, 2)
        self.assertEqual(result, 1)
    
    def test_addition_of_zero_and_positive_numbers(self):
        result = add(0, 2)
        self.assertEqual(result, 2)
    
    def test_addition_of_zero_and_negative_numbers(self):
        result = add(0, -2)
        self.assertEqual(result, -2)
    
    def test_addition_big_numbers(self):
        result = add(100000, 200000)
        self.assertEqual(result, 300000)
    
    def test_addition_of_floats(self):
        result = add(1.1, 2.2)
        self.assertEqual(result, 3.3)
    
    def test_addition_of_negative_floats(self):
        result = add(-1.1, -2.2)
        self.assertEqual(result, -3.3)
    
    def test_subtraction(self):
        result = subtract(2, 1)
        self.assertEqual(result, 1)
    
    def test_subtraction_of_negative_numbers(self):
        result = subtract(-1, -2)
        self.assertEqual(result, 1)
    
    def test_subtraction_of_positive_and_negative_numbers(self):
        result = subtract(-1, 2)
        self.assertEqual(result, -3)
    
    def test_subtraction_of_zero_and_positive_numbers(self):
        result = subtract(0, 2)
        self.assertEqual(result, -2)
    
    def test_subtraction_of_zero_and_negative_numbers(self):
        result = subtract(0, -2)
        self.assertEqual(result, 2)
    
    def test_subtraction_big_numbers(self):
        result = subtract(100000, 200000)
        self.assertEqual(result, -100000)
    
    def test_subtraction_of_floats(self):
        result = subtract(2.2, 1.1)
        self.assertEqual(result, 1.1)
    
    def test_subtraction_of_negative_floats(self):
        result = subtract(-2.2, -1.1)
        self.assertEqual(result, -1.1)
    
    def test_multiplication(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)
    
    def test_division(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
    
    def test_addition_of_floats(self):
        result = add(1.1, 2.2)
        self.assertEqual(result, 3.3)
    
    def test_subtraction_of_floats(self):
        result = subtract(2.2, 1.1)
        self.assertEqual(result, 1.1)
    
    def test_multiplication_of_floats(self):
        result = multiply(2.2, 3.3)
        self.assertEqual(result, 7.26)
    
    def test_division_of_floats(self):
        result = divide(6.6, 2.2)
        self.assertEqual(result, 3.0)
    
    # def test_division_by_zero_floats(self):
    #     result = divide(1.1, 0)
    #     self.assertEqual(result, float('inf'))




if __name__ == '__main__':
    unittest.main()
