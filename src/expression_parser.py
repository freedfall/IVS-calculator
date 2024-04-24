## 
# @file expression_parser.py
# @brief Expression parser implementation 
# @Author: Sviatoslav Shishnev
# @Author: Artem Dvorychanskyi
##

import re
import traceback
from calc import *

class Stack:
    """
    Represents a stack data structure for the expression parser.
    """
    def __init__(self):
        """
        Initializes an empty stack with an END terminal item.
        """
        self.items = [] 
        self.items.append(self.create_item(token_type="END", item_type="T"))

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Pushes an item onto the stack.

        Args:
            item (dict): The item to push onto the stack.
        """
        self.items.append(item)

    def top_terminal(self):
        """
        Returns the topmost terminal item from the stack.

        Returns:
            dict: The topmost terminal item.
        
        Raises:
            IndexError: If the stack is empty or if no terminal item is found.
        """
        if not self.is_empty():
            reversed_list = reversed(self.items)
            for item in reversed_list:
                if item["item_type"] == "T": # T is for terminal 
                    return item
        raise IndexError("Top function performed on empty stack or terminal was not found")
    
    def find_index_of_terminal(self):
        """
        Finds the index of the topmost terminal item in the stack.

        Returns:
            int: The index of the topmost terminal item in the stack.
        """
        reversed_list = list(reversed(self.items))
        for i in range(len(reversed_list)):
            if reversed_list[i]["item_type"] == "T": # T is for terminal 
                return len(self.items) - i 
            
    def pop(self, index=None):
        """
        Pops an item from the stack.

        Args:
            index (int, optional): The index of the item to pop. Defaults to None, which pops the top item.

        Returns:
            dict: The popped item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            if index != None:
                return self.items.pop(index)
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def str_to_digit_converter(self, string):
        """
        Converts a string representation of a number to either an integer or a float.

        Args:
            string (str): The string representation of the number.

        Returns:
            int or float: The converted number.
        """
        if re.search(r'.*\..*', string):
            value = float(string)
        else:
            value = int(string)
        return value

    def reduce_rule(self): 
        """
        Reduces the stack based on certain reduction rules.

        Returns:
            bool: True if a reduction rule was applied, False otherwise.
        """
        reversed_items = list(reversed(self.items))
        for i in range(self.size()):
            if reversed_items[i]["item_type"] == "CATCH":
                if i == 3 and ( list(reversed(self.items))[1]["item_type"] != "NT" ):
                    operator = list(reversed(self.items))[1]["value"]
                    a = list(reversed(self.items))[2]["value"]
                    b = list(reversed(self.items))[0]["value"]
                    match operator:
                        case "+":
                            new_value = add(a, b)
                        case "-":
                            new_value = subtract(a, b)
                        case "/":
                            new_value = divide(a, b)
                        case "*": 
                            new_value = multiply(a, b)
                        case "%":
                            new_value = modulo(a, b)
                    for i in range(4):
                        self.items.pop()
                elif i == 3:
                    new_value = list(reversed(self.items))[1]["value"]
                    for i in range(4):
                        self.items.pop()
                elif i == 2 and list(reversed(self.items))[0]["token_type"] == "OP3":
                        value = list(reversed(self.items))[1]["value"]
                        if isinstance(value, float):
                            if value.is_integer():  # Check if the float value is already an integer
                                value = int(value) 
                        new_value = factorial(value)
                        for i in range(3):
                            self.items.pop()
                elif i == 1:
                    tt = list(reversed(self.items))[0]["token_type"]
                    if tt == "ID":
                        new_value = list(reversed(self.items))[0]["value"]
                    elif tt == "POWER" or tt == "ROOT":
                        data = list(reversed(self.items))[0]["value"][2:-1]
                        data = data.split(',', 1)
                        subanalyser = Analyser()
                        expr = subanalyser.analyse(data[1])
                        if isinstance(expr,bool) and expr == False:
                            raise ValueError(f'error in function arguments') 
                        if tt == "POWER":
                            new_value = power(self.str_to_digit_converter(data[0]), expr)
                        else:
                            new_value = root(expr, self.str_to_digit_converter(data[0]))
                    for i in range(2): 
                        self.items.pop()
                else: 
                    return False
                new_nonterminal = self.create_item(item_type="NT", value=new_value) 
                self.push(new_nonterminal)
                return True
        return False

    def size(self):
        """
        Returns the size of the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self.items)
    
    def create_item( self, item_type="UN", value="", token_type=""):
        """
        Creates a new item for the stack.

        Args:
            item_type (str, optional): The type of the item. Defaults to "UN".
            value (str, optional): The value of the item. Defaults to "".
            token_type (str, optional): The token type of the item. Defaults to "".

        Returns:
            dict: The newly created item.
        """
        return { 'item_type': item_type, 'value': value, "token_type": token_type}

class Analyser:
    """
    Represents an expression analyser.
    """

    def __init__(self):
        """
        Initializes the expression analyser with a stack and expression tables.
        """
        self.stack = Stack()
        self.exp_table = [
            # "+", "*", "(", ")", "id", "$", "!"
            [">", "<", "<", ">", "<", ">", "<"],   # "+"
            [">", ">", "<", ">", "<", ">", "<"],   # "*"
            ["<", "<", "<", "=", "<", "E", "<"],   # "("
            [">", ">", "E", ">", "E", ">", ">"],   # ")"
            [">", ">", "E", ">", "E", ">", ">"],   # "id"
            ["<", "<", "<", "E", "<", "F", "<"],   # "$"
            [">", ">", "E", ">", "E", ">", "E"]
        ]
        self.symbol_to_index_map = {
            "OP1" : 0,
            "OP2" : 1,
            "OP3" : 6,
            "OPAR" : 2,
            "CPAR" : 3, 
            "ID" : 4,
            "ROOT" : 4,
            "POWER": 4,
            "END" : 5,
        }

    def reinitialize_stack(self):
        """
        Reinitializes the stack.
        """
        self.stack = Stack()

    def tokenize(self, expression):
        """
        Tokenizes the input expression.

        Args:
            expression (str): The input expression.

        Returns:
            list: The list of tokens.
        """
        expression = expression.replace(" ",'')
        tokens = []
        regex_pattern = r"([-+*/%!])|(\d+(\.\d+)?)|(\()|(\)|([rp]\[[^\]]+\]))"

        # Iterate through the expression using re.finditer to handle overlapping matches
        for match in re.finditer(regex_pattern, expression):
            if match.group(1):
                char = match.group(1)
                if char in '+-':
                    token_type = "OP1"  # Operator type 1: + or -
                elif char in '*/%':
                    token_type = "OP2"  # Operator type 2: * or /
                elif char in '!':
                    token_type = "OP3"  # Operator type 2: * or /
            elif match.group(2):
                # Numeric value found (integer or float)
                token_type = "ID"
            elif match.group() == "(":
                token_type = "OPAR"
            elif match.group() == ")":
                token_type = "CPAR"
            elif match.group(5):
                if match.group(5)[0] == 'r':
                    token_type = "ROOT"
                else: 
                    token_type = "POWER"
            else:
                raise ValueError(f'Error tokenizing')
            value = match.group()
            if token_type == "ID":
                value = self.stack.str_to_digit_converter(value)
            tokens.append({'item_type': 'T', 'value': value, 'token_type': token_type})

        # Append END token at the end of the token stream
        tokens.append({'item_type': 'T', 'value': '$', 'token_type': 'END'})

        return tokens
    
    def access_table(self, token):
        """
        Accesses the expression table based on the input token.

        Args:
            token (dict): The token to access the expression table.

        Returns:
            str: The entry in the expression table.
        """
        stack_symbol = self.stack.top_terminal()["token_type"]
        return self.exp_table[self.symbol_to_index_map[stack_symbol]][self.symbol_to_index_map[token]]

    def analyse(self, expr):
        """
        Analyzes the input expression.

        Args:
            expr (str): The input expression.

        Returns:
            bool or int or float: The result of the analysis.
        """
        try:
            result = self.analyse_tokens(self.tokenize(expr))
        except:
            return False
        if result[0] == True:
            return result[1]
        else:
            return False

    def analyse_tokens(self, token_stream):
        """
        Analyzes a stream of tokens.

        Args:
            token_stream (list): The stream of tokens.

        Returns:
            list: A list indicating the success of the analysis and its result.
        """
        for token in token_stream:
            try:
                result = self.handleToken(token)
            except Exception as e:
                return [False, e.args]    
        return [True, result]
    
    def handleToken(self, token):
        """
        Handles a single token.

        Args:
            token (dict): The token to handle.

        Returns:
            int or float: The result of handling the token.

        Raises:
            ValueError: If an error occurs while handling the token.
        """
        symbol = self.access_table(token["token_type"])
        if symbol == ">":
            if not(self.stack.reduce_rule()):
                raise ValueError(f'Error while reducing rule happend')
            return self.handleToken(token)
        elif symbol == "<":
            self.stack.items.insert(self.stack.find_index_of_terminal(),self.stack.create_item(item_type="CATCH")) # CATCH is for cath symbol
            self.stack.push(token)
        elif symbol == "=":
            self.stack.push(token)
        elif symbol == "F":
            if self.stack.size() == 2:
                return self.stack.items[1]["value"]
        elif symbol == "E":
            raise ValueError(f'Error in handleToken with token: {token, self.stack.top_terminal()["token_type"]}')