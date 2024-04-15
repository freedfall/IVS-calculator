import unittest
from expression_parser import Analyser  # Assuming Analyzer class is defined in analyser.py

class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.analyser = Analyser()  # Create an instance of Analyser before each test

    def test_tokenize_basic_expression(self):
        # Test tokenization of a basic arithmetic expression
        expression = "112 + 12.2 - 5 * 3 / 7 - 2"
        expected_tokens = [
            {'item_type': 'T', 'value': '112', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '+', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '12.2', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '5', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '*', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': '3', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '/', 'token_type': 'OP2'},
            {'item_type': 'T', 'value': '7', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '-', 'token_type': 'OP1'},
            {'item_type': 'T', 'value': '2', 'token_type': 'ID'},
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
            {'item_type': 'T', 'value': '5', 'token_type': 'ID'},
            {'item_type': 'T', 'value': '$', 'token_type': 'END'}
        ]
        token_stream = self.analyser.tokenize(expression)
        self.assertEqual(token_stream, expected_tokens)

if __name__ == '__main__':
    unittest.main()
