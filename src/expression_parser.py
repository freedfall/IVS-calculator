## 
# @file expression_parser.py
# @brief Expression parser implementation 
# @Author: Svaitoslav Shishnev
# @Author: Artem Dvorychanskiy
##

class Stack:
    def __init__(self):
        self.items = [[], []]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def top_terminal(self):
        if not self.is_empty():
            reversed_list = self.items.reverse
            for item in reversed_list:
                if item[1] == "T": # T is for terminal 
                    return item
        else:
            raise IndexError("top function performed on empty stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # or raise an IndexError
        
    def reduce_rule(self): 

        return

    def size(self):
        return len(self.items)

class Analyzer:

    def __init__(self):
        self.stack = Stack()
        self.exp_table = [
           #["+", "-", "/", "*", "$"]
            [">", ">", "<", "<", ">"], # + 
            [">", ">", "<", "<", ">"], # -
            [">", ">", ">", ">", ">"], # /
            [">", ">", ">", ">", ">"], # *
            ["<", "<", "<", "<", "E"], # $
        ]

    def access_table(self, token):
        stack_symbol = self.stack.top_terminal()
        return self.exp_table[stack_symbol][token]

    def analyze(self, token):
        self.handleToken(token)
    
    def handleToken(self, token):
        symbol = self.access_table(token)
        if symbol == ">":
            self.stack.reduce_rule()
        elif symbol == "<":
            self.stack.push("C") # C is for cath symbol
            self.stack.push(token)
        elif symbol == "=":
            self.stack.push(token)
        elif symbol == "E":
            raise ValueError(f'Error in handleToken with token: {token}')