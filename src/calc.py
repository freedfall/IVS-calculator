## 
# @file calc.py
# @brief math library
# @Author: Timur Kininbayev
# @Author: Artem Dvorychanskiy
##

### ADD FUNCTION ###
def add(a, b):
    return round(a + b , 6)

### SUBTRACT FUNCTION###
def subtract(a, b):
    return round(a - b , 6)

### MULTIPLY FUNCTION ###
def multiply(a, b):
    return round(a * b , 6)


### DIVISION FUNCTION ###
def divide(a, b):
    return round(a / b , 6)


### MODULO FUNCTION ###
def modulo(a, b):
    return round(a % b , 6)


### POWER FUNCTION ###
def power(a, b):
    if (a == 0):
        return 0
    return round(a ** b , 6)


### FACTORIAL FUNCTION ###
def factorial(a):
    if(a < 0):
        raise ValueError("Cannot calculate factorial of negative numbers")
    if(type(a) != int):
        raise ValueError("Factorial function can only accept integers")
    if a == 0:
        return 1
    else:
        return round(a * factorial(a - 1) , 6)


### SQUARE ROOT FUNCTION ###
def root(a, b):
    # Check if the index (b) is zero
    if b == 0:
        raise ValueError("The index (b) cannot be zero.")
    
    # Check if base (a) is negative and index (b) is even
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot compute the even root of a negative number.")
    
    # Calculate the b-th root of a
    if a == 0:
        return 0
    
    return round(a ** (1 / b), 6)
