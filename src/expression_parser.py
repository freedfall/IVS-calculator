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
        
    def str_to_digit_converter(self, string):
        if re.search(r'.*\..*', string):
            value = float(string)
        else:
            value = int(string)
        return value

    def reduce_rule(self): 
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
                        print(data)
                        subanalyser = Analyser()
                        base = subanalyser.analyse(data[0])
                        subanalyser.reinitialize_stack()
                        exponent = subanalyser.analyse(data[1])
                        print(base, exponent)
                        if (isinstance(base, bool) and base == False) or (isinstance(exponent, bool) and exponent == False) :
                            raise ValueError(f'error in function arguments') 
                        if tt == "POWER":
                            
                            new_value = power(base, exponent)
                        else:
                            new_value = root(base, exponent)
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
        self.stack = Stack()

    def tokenize(self, expression):
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
        stack_symbol = self.stack.top_terminal()["token_type"]
        return self.exp_table[self.symbol_to_index_map[stack_symbol]][self.symbol_to_index_map[token]]

    def analyse(self, expr):
        try:
            result = self.analyse_tokens(self.tokenize(expr))
        except:
            return False
        if result[0] == True:
            return result[1]
        else:
            return False

    def analyse_tokens(self, token_stream):
        for token in token_stream:
            try:
                result = self.handleToken(token)
            except Exception as e:
                return [False, e.args]    
        return [True, result]
    
    def handleToken(self, token):
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