import unittest
from unittest.mock import patch
from io import StringIO
import profile_stddev  # Assuming your main script is named 'profile.py'

class TestStandardDeviationCalculator(unittest.TestCase):
    def test_read_numbers(self):
        user_input = '1 2 3 4 5\n6 7 8 9 10\n'
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with patch('sys.stdin', StringIO(user_input)):
            result = profile_stddev.read_numbers()
        self.assertEqual(result, expected_output)

    def test_calculate_mean(self):
        numbers = [1, 2, 3, 4, 5]
        expected_mean = 3.0
        result = profile_stddev.calculate_mean(numbers)
        self.assertEqual(result, expected_mean)

    def test_calculate_variance(self):
        numbers = [1, 2, 3, 4, 5]
        mean = 3.0
        expected_variance = 2.5
        result = profile_stddev.calculate_variance(numbers, mean)
        self.assertEqual(result, expected_variance)

    def test_calculate_standard_deviation(self):
        variance = 2.5
        expected_std_dev = 1.5811388300841898  # This is the square root of 2.5
        result = profile_stddev.root(variance,2)  # Assuming sqrt is a static method in calc module
        print(result)
        self.assertAlmostEqual(result, expected_std_dev)

if __name__ == '__main__':
    unittest.main()
