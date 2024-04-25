## 
# @file test.py
# @brief Test cases for the math library
# @author: Sviatoslav Shisnev
##

import unittest
from expression_parser import Analyser

class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.analyser = Analyser()  # Create an instance of analyser before each test
    
    def test_simple_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': '112', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '12.2', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertTrue(self.analyser.analyse_tokens(token_stream))

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
        self.assertTrue(self.analyser.analyse_tokens(token_stream))

    def test_invalid_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': 12, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': 12, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertFalse(self.analyser.analyse_tokens(token_stream)[0])

    def test_empty_expression(self):
        token_stream = [
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        self.assertTrue(self.analyser.analyse_tokens(token_stream))

if __name__ == '__main__':
    unittest.main()
