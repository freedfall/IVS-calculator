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
        token_stream = [
            {'item_type': 'T', 'value': '112', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '12.2', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertTrue(self.analyzer.analyze(token_stream))

    def test_complex_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': 12, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': 5, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': 30, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': 7.8, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertTrue(self.analyzer.analyze(token_stream))

    def test_invalid_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': 'id', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': 'id', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertFalse(self.analyzer.analyze(token_stream))

    def test_empty_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertTrue(self.analyzer.analyze(token_stream))

if __name__ == '__main__':
    unittest.main()
