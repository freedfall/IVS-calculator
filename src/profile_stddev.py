import sys
from calc import add, multiply, root, divide,power

def read_numbers():
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(float, line.split()))
    return numbers

def calculate_mean(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    return divide(total_sum,count)

def calculate_variance(numbers, mean):
    sum_of_squares = sum(power((x - mean), 2) for x in numbers) 
    return divide(sum_of_squares, (len(numbers) - 1))

def result(numbers):
    mean = calculate_mean(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = root(variance, 2)  # Using the new sqrt function from calc
    return round(standard_deviation,7)

def main():
    numbers = read_numbers()
    print(result(numbers))
    
if __name__ == "__main__":
    main()
