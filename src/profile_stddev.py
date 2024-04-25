##
# @file profile_stddev.py
# @brief This script calculates the standard deviation of a series of numbers
# @author Artem Dvorychanskyi
##

import sys
from calc import add, multiply, root, divide, power

## @brief Reads numbers from the standard input
# @return A list of numbers
def read_numbers():
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(float, line.split()))
    return numbers

## @brief Calculates the mean of a list of numbers
# @param numbers A list of numbers
# @return The mean of the numbers
def calculate_mean(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    return divide(total_sum, count)

## @brief Calculates the variance of a list of numbers
# @param numbers A list of numbers
# @param mean The mean of the numbers
# @return The variance of the numbers
def calculate_variance(numbers, mean):
    sum_of_squares = sum(power((x - mean), 2) for x in numbers) 
    return divide(sum_of_squares, (len(numbers) - 1))

## @brief Calculates the standard deviation of a list of numbers
# @param numbers A list of numbers
# @return The standard deviation of the numbers
def result(numbers):
    mean = calculate_mean(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = root(variance, 2)  # Using the new sqrt function from calc
    return round(standard_deviation, 7)

## @brief Main function
# Reads numbers from the standard input, calculates their standard deviation, and prints the result
def main():
    numbers = read_numbers()
    print(result(numbers))
    
if __name__ == "__main__":
    main()