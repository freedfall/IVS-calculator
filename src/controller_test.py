## 
# @file test_analyser.py
# @brief Test cases for analyser behaviour 
# @author Sviatoslav Shishnev
##

import unittest
from logic import controller

## 
# @brief Test class for the controller.
# @details This class contains unit tests for the controller.
##
class TestController(unittest.TestCase):

    ## 
    # @brief Test case for basic binary to decimal conversion.
    # @details This test case checks if the binary expression "101+110*10/1" is correctly converted to "5+6*2/1".
    ##
    def test_basic(self):
        expr = "101+110*10/1"
        self.assertEqual('5+6*2/1', (controller.convertBinaryToDecimal(expr)))

    ## 
    # @brief Test case for binary to decimal conversion with parentheses.
    # @details This test case checks if the binary expression "(101+110)*10/1" is correctly converted to "(5+6)*2/1".
    ##
    def test_par(self):
        expr = "(101+110)*10/1"
        self.assertEqual('(5+6)*2/1', (controller.convertBinaryToDecimal(expr)))

if __name__ == '__main__':
    unittest.main()