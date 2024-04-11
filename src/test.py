## 
# @file test.py
# @brief Test cases for the math library
# @Author: Timur Kininbayev
# @Author: Artem Dvorychanskiy
##

#Imports
import unittest
from src import calc

#Functions
class TestMathLibrary(unittest.TestCase):

    ##### Add function tests #####
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
    
    ##### Subtract function tests #####
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
    
    ##### Multiply function tests #####
    def test_multiplication(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)
    
    def test_multiplication_of_negative_numbers(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)
    
    def test_multiplication_of_positive_and_negative_numbers(self):
        result = multiply(-2, 3)
        self.assertEqual(result, -6)
    
    def test_multiplication_of_zero_and_positive_numbers(self):
        result = multiply(0, 3)
        self.assertEqual(result, 0)
    
    def test_multiplication_of_zero_and_negative_numbers(self):
        result = multiply(0, -3)
        self.assertEqual(result, 0)
    
    def test_multiplication_big_numbers(self):
        result = multiply(100000, 200)
        self.assertEqual(result, 20000000)
    
    def test_multiplication_of_floats(self):
        result = multiply(2.2, 3.3)
        self.assertEqual(result, 7.26)
    
    def test_multiplication_of_negative_floats(self):
        result = multiply(-2.2, -3.3)
        self.assertEqual(result, 7.26)
    
    ##### Division function tests #####
    def test_division(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
        
    def test_division_of_negative_numbers(self):
        result = divide(-6, -2)
        self.assertEqual(result, 3)
    
    def test_division_of_positive_and_negative_numbers(self):
        result = divide(-6, 2)
        self.assertEqual(result, -3)
    
    def test_division_of_zero_and_positive_numbers(self):
        result = divide(0, 2)
        self.assertEqual(result, 0)
    
    def test_division_of_zero_and_negative_numbers(self):
        result = divide(0, -2)
        self.assertEqual(result, 0)
    
    def test_division_big_numbers(self):
        result = divide(20000000, 200)
        self.assertEqual(result, 100000)
    
    def test_division_of_floats(self):
        result = divide(7.26, 3.3)
        self.assertEqual(result, 2.2)
    
    def test_division_of_negative_floats(self):
        result = divide(-7.26, -3.3)
        self.assertEqual(result, 2.2)
    
    ##### Power function tests #####
    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)
    
    def test_power_of_negative_numbers(self):
        result = power(-2, 3)
        self.assertEqual(result, -8)
    
    def test_power_of_positive_and_negative_numbers(self):
        result = power(-2, 3)
        self.assertEqual(result, -8)
    
    def test_power_of_zero_and_positive_numbers(self):
        result = power(0, 3)
        self.assertEqual(result, 0)
    
    def test_power_of_zero_and_negative_numbers(self):
        result = power(0, -3)
        self.assertEqual(result, 0)
    
    def test_power_big_numbers(self):
        result = power(200, 3)
        self.assertEqual(result, 8000000)
    
    def test_power_of_floats(self):
        result = power(2.2, 3)
        self.assertEqual(result, 10.648)
    
    def test_power_of_negative_floats(self):
        result = power(-2.2, 3)
        self.assertEqual(result, -10.648)

    ##### Square root function tests #####
    def test_square_root(self):
        result = square_root(9)
        self.assertEqual(result, 3)
    
    def test_square_root_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            square_root(-9)
    
    def test_square_root_of_zero(self):
        result = square_root(0)
        self.assertEqual(result, 0)
    
    def test_square_root_of_floats(self):
        result = square_root(9.0)
        self.assertEqual(result, 3)
    
    def test_square_root_of_negative_floats(self):
        with self.assertRaises(ValueError):
            square_root(-9.0)

    ##### Factorial function tests #####
    def test_factorial(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_of_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_floats(self):
        with self.assertRaises(ValueError):
            factorial(5.0)

    def test_factorial_of_negative_floats(self):
        with self.assertRaises(ValueError):
            factorial(-5.0)
    
           
if __name__ == '__main__':
    unittest.main()
