## 
# @file calc.py
# @brief math library
# @Author: Timur Kininbayev
# @Author: Artem Dvorychanskiy
##

### ADD FUNCTION ###
def add(a, b):
    return round(a + b , 5)

### SUBTRACT FUNCTION###
def subtract(a, b):
    return round(a - b , 5)

### MULTIPLY FUNCTION ###
def multiply(a, b):
    return round(a * b , 5)


### DIVISION FUNCTION ###
def divide(a, b):
    return round(a / b , 5)


### MODULO FUNCTION ###
def modulo(a, b):
    return round(a % b , 5)


### POWER FUNCTION ###
def power(a, b):
    if (a == 0):
        return 0
    return round(a ** b , 5)


### FACTORIAL FUNCTION ###
def factorial(a):
    if(a < 0):
        raise ValueError("Cannot calculate factorial of negative numbers")
    if(type(a) != int):
        raise ValueError("Factorial function can only accept integers")
    if a == 0:
        return 1
    else:
        return round(a * factorial(a - 1) , 5)


### SQUARE ROOT FUNCTION ###
def root(a, b):

    if(b == 0):
        raise ValueError("Cannot calculate square root with 0 as a power")
    
    if(a < 0 and b % 2 == 0):
        raise ValueError("Cannot calculate square root of negative numbers")
    
    return round(a ** (1/b) , 5)
    

