## 
# @file calc.py
# @brief math library
# @Author: Timur Kininbayev
# @Author: Artem Dvorychanskiy
##

### ADD FUNCTION ###
def add(a, b):
    return a + b

### SUBTRACT FUNCTION###
def substract(a, b):
    return a - b

### MULTIPLY FUNCTION ###
def multiply(a, b):
    return a * b


### DIVISION FUNCTION ###
def division(a, b):
    return a / b


### MODULO FUNCTION ###
def modulo(a, b):
    return a % b


### POWER FUNCTION ###
def power(a, b):
    return a ** b


### FACTORIAL FUNCTION ###
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


### SQUARE ROOT FUNCTION ###
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative numbers")
    return a ** 0.5

