## 
# @file expression_parser.py
# @brief Expression parser implementation 
# @Author: Svaitoslav Shishnev
# @Author: Artem Dvorychanskiy
##

import re
import traceback
from calc import *

 

class Stack:
    def __init__(self):
        self.items = [] 
        self.items.append(self.create_item(token_type="END", item_type="T"))

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def top_terminal(self):
        if not self.is_empty():
            reversed_list = reversed(self.items)
            for item in reversed_list:
                if item["item_type"] == "T": # T is for terminal 
                    return item
        raise IndexError("Top function performed on empty stack or terminal was not found")
    def find_index_of_terminal(self):
        reversed_list = list(reversed(self.items))
        for i in range(len(reversed_list)):
            if reversed_list[i]["item_type"] == "T": # T is for terminal 
                return len(self.items) - i 
    def pop(self, index=None):
        if not self.is_empty():
            if index != None:
                return self.items.pop(index)
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def reduce_rule(self): 
        reversed_items = list(reversed(self.items))
        for i in range(self.size()):
            if reversed_items[i]["item_type"] == "CATCH":
                if i == 3:
                    operator = list(reversed(self.items))[1]["value"]
                    a = list(reversed(self.items))[2]["value"]
                    b = list(reversed(self.items))[0]["value"]
                    match operator:
                        case "+":
                            new_value = add(a, b)
                        case "-":
                            new_value = substract(a, b)
                        case "/":
                            new_value = division(a, b)
                        case "*": 
                            new_value = multiply(a, b)
                    for i in range(4):
                        self.items.pop()
                elif i == 1 and list(reversed(self.items))[0]["token_type"] == "ID":
                    new_value = list(reversed(self.items))[0]["value"]
                    for i in range(2): 
                        self.items.pop()
                else: 
                    return False
                new_nonterminal = self.create_item(item_type="NT", value=new_value) 
                self.push(new_nonterminal)
                return True
        return False

    def size(self):
        return len(self.items)
    
    def create_item( self, item_type="UN", value="", token_type=""):
        return { 'item_type': item_type, 'value': value, "token_type": token_type}

class Analyser:

    def __init__(self):
        self.stack = Stack()
        self.exp_table = [
           # "+", "*", "id", "$"
            [">", "<", "<", ">"],   # "+"
            [">", ">", "<", ">"],   # "*"
            [">", ">", "E", ">"],   # "id"
            ["<", "<", "<", "F"],   # "$"
        ]
        self.symbol_to_index_map = {
            "OP1" : 0,
            "OP2" : 1, 
            "ID" : 2,
            "END" : 3,
        }


    def tokenize(self, expression):
        expression = expression.replace(" ",'')
        tokens = []
        regex_pattern = r"([-+*/])|(\d+(\.\d+)?)"

        # Iterate through the expression using re.finditer to handle overlapping matches
        for match in re.finditer(regex_pattern, expression):
            if match.group(1):
                char = match.group(1)
                if char in '+-':
                    token_type = "OP1"  # Operator type 1: + or -
                elif char in '*/':
                    token_type = "OP2"  # Operator type 2: * or /
            elif match.group(2):
                # Numeric value found (integer or float)
                token_type = "ID"

            value = match.group()
            tokens.append({'item_type': 'T', 'value': value, 'token_type': token_type})

        # Append END token at the end of the token stream
        tokens.append({'item_type': 'T', 'value': '$', 'token_type': 'END'})

        return tokens


    def access_table(self, token):
        stack_symbol = self.stack.top_terminal()["token_type"]
        return self.exp_table[self.symbol_to_index_map[stack_symbol]][self.symbol_to_index_map[token]]

    def analyse_tokens(self, token_stream):
        for token in token_stream:
            try:
                self.handleToken(token)
            except Exception as e:
                traceback.print_exc()
                return False    
        return True
    def handleToken(self, token):
        symbol = self.access_table(token["token_type"])
        if symbol == ">":
            if not(self.stack.reduce_rule()):
                raise ValueError(f'Error while reducing rule happend')
            self.handleToken(token)
        elif symbol == "<":
            self.stack.items.insert(self.stack.find_index_of_terminal(),self.stack.create_item(item_type="CATCH")) # CATCH is for cath symbol
            self.stack.push(token)
        elif symbol == "=":
            self.stack.push(token)
        elif symbol == "F":
            if self.stack.size() == 3:
                return self.stack.items[1]["value"]
            self.stack = Stack()
        elif symbol == "E":
            raise ValueError(f'Error in handleToken with token: {token, self.stack.top_terminal()["token_type"]}')