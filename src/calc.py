## 
# @file calc.py
# @brief A library of mathematical functions.
# @author Timur Kininbayev
# @author Artem Dvorychanskyi
##

## 
# @brief Adds two numbers.
# @param a The first number.
# @param b The second number.
# @return The sum of a and b.
##
def add(a, b):
    return round(a + b , 6)

## 
# @brief Subtracts one number from another.
# @param a The first number.
# @param b The number to subtract from a.
# @return The result of a minus b.
##
def subtract(a, b):
    return round(a - b , 6)

## 
# @brief Multiplies two numbers.
# @param a The first number.
# @param b The second number.
# @return The product of a and b.
##
def multiply(a, b):
    return round(a * b , 6)

## 
# @brief Divides one number by another.
# @param a The dividend.
# @param b The divisor.
# @return The quotient of a and b.
##
def divide(a, b):
    return round(a / b , 6)

## 
# @brief Calculates the modulo of two numbers.
# @param a The dividend.
# @param b The divisor.
# @return The remainder of a divided by b.
##
def modulo(a, b):
    return round(a % b , 6)

## 
# @brief Raises a number to a power.
# @param a The base.
# @param b The exponent.
# @return The result of a raised to the power of b.
##
def power(a, b):
    if (a == 0):
        return 0
    return round(a ** b , 6)

## 
# @brief Calculates the factorial of a number.
# @param a The number.
# @return The factorial of a.
##
def factorial(a):
    if(a < 0):
        raise ValueError("Cannot calculate factorial of negative numbers")
    if(type(a) != int):
        raise ValueError("Factorial function can only accept integers")
    if a == 0:
        return 1
    else:
        return round(a * factorial(a - 1) , 6)

## 
# @brief Calculates the b-th root of a number.
# @param a The base.
# @param b The index.
# @return The b-th root of a.
##
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