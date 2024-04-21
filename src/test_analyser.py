## 
# @file test_analyser.py
# @brief Test cases for analyser behaviour 
# @Author: Sviatoslav Shishnev
##

import unittest
from expression_parser import Analyser

class TestAnalyserclass(unittest.TestCase):
    def setUp(self):
        self.analyser = Analyser() 
    
    def test_simple_expression(self):
        expr = '12+34- 28.8 * 100'
        self.assertEqual(-2834,(self.analyser.analyse(expr)))

    def test_single_expression(self):
        expr = '1.0'
        self.assertEqual(1.0,(self.analyser.analyse(expr)) )
        
    def test_par(self):
        expr = '(12+2)*2'
        self.assertEqual(28, (self.analyser.analyse(expr)))
    
    def test_single_par(self):
        expr = "()"
        self.assertEqual(False, (self.analyser.analyse(expr))) 

if __name__ == '__main__':
    unittest.main()
