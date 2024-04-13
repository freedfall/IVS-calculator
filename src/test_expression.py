## 
# @file test.py
# @brief Test cases for the math library
# @Author: Sviatoslav Shisnev
##

import unittest
from expression_parser import Analyzer

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = Analyzer()  # Create an instance of Analyzer before each test

    def test_simple_expression(self):
        token_stream = ["id", "+", "id", "$"]
        self.assertIsNone(self.analyzer.analyze(token_stream))

    def test_complex_expression(self):
        token_stream = ["id", "+", "id", "*", "id", "-", "id", "$"]
        self.assertIsNone(self.analyzer.analyze(token_stream))

    def test_invalid_expression(self):
        token_stream = ["id", "+", "*", "id", "$"]  # Invalid: consecutive operators
        with self.assertRaises(ValueError):
            self.analyzer.analyze(token_stream)

    def test_empty_expression(self):
        token_stream = ["$"]  # Just the end marker
        self.assertIsNone(self.analyzer.analyze(token_stream))

if __name__ == '__main__':
    unittest.main()
