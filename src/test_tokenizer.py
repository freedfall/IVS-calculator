##
# @file test_analyser.py
#
# @brief Unit tests for the Analyser class in the expression_parser module.
#
# @author Artem Dvorychanskyi
##

import unittest
from expression_parser import Analyser  # Assuming Analyzer class is defined in analyser.py

class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.analyser = Analyser()  # Create an instance of Analyser before each test

    def test_tokenize_basic_expression(self):
        # Test tokenization of a basic arithmetic expression
        expression = "112 + 12.2 - 5 * 3 / 7 - 2"
        expected_tokens = [
            {'item_type': 'T', 'value': 112, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': 12.2, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': 5, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': 3, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '/', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': 7, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': 2, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        # Tokenize the expression using the tokenize method of the Analyser class
        token_stream = self.analyser.tokenize(expression)
        # Compare the actual token stream with the expected tokens
        self.assertEqual(token_stream, expected_tokens)

    def test_tokenize_single_digit_expression(self):
        # Test tokenization of an expression containing a single digit
        expression = "5"
        expected_tokens = [
            {'item_type': 'T', 'value': 5, 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        token_stream = self.analyser.tokenize(expression)
        self.assertEqual(token_stream, expected_tokens)


    def test_tokenize_power_operator(self):
        # Test tokenization of an expression with the power operator (^)
        expression = "p[2,3]"
        expected_tokens = [
            {'item_type': 'T', 'value': "p[2,3]", 'token_type': 'POWER'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        token_stream = self.analyser.tokenize(expression)
        self.assertEqual(token_stream, expected_tokens)

    def test_tokenize_r_function(self):
        # Test tokenization of an expression with r[...] function
        expression = "r[variable]"
        expected_tokens = [
            {'item_type': 'T', 'value': 'r[variable]', 'token_type': 'ROOT'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        token_stream = self.analyser.tokenize(expression)
        self.assertEqual(token_stream, expected_tokens)

    def test_tokenize_complex_expression(self):
        # Test tokenization of a complex arithmetic expression
        expression = "(2-3)*(3-5)"
        expected_tokens = [
            {'item_type': 'T', 'value': '(', 'token_type': 'OPAR'},  # (
            {'item_type': 'T', 'value': 2, 'token_type': 'ID'},       # 2
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},     # -
            {'item_type': 'T', 'value': 3, 'token_type': 'ID'},       # 3
            {'item_type': 'T', 'value': ')', 'token_type': 'CPAR'},  # )
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},     # *
            {'item_type': 'T', 'value': '(', 'token_type': 'OPAR'},  # (
            {'item_type': 'T', 'value': 3, 'token_type': 'ID'},       # 3
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},     # -
            {'item_type': 'T', 'value': 5, 'token_type': 'ID'},       # 5
            {'item_type': 'T', 'value': ')', 'token_type': 'CPAR'},  # )
            {'item_type': 'T', 'value': '$', 'token_type': 'END'},     # End of expression
        ]
        
        # Tokenize the expression using the tokenize method of the Analyser class
        token_stream = self.analyser.tokenize(expression)
        # Compare the actual token stream with the expected tokens
        self.assertEqual(token_stream, expected_tokens)

if __name__ == '__main__':
    unittest.main()
