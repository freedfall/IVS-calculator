## 
# @file test_analyser.py
# @brief Test cases for analyser behaviour 
# @Author: Sviatoslav Shishnev
##

import unittest
from logic import controller

class TestController(unittest.TestCase):
    def test_basic(self):
        expr = "101+110*10/1"
        self.assertEqual('5+6*2/1', (controller.convertBinaryToDecimal(expr)))
    def test_par(self):
        expr = "(101+110)*10/1"
        self.assertEqual('(5+6)*2/1', (controller.convertBinaryToDecimal(expr)))
if __name__ == '__main__':
    unittest.main()
