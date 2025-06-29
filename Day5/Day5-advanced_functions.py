
# advanced_functions.py
# ---------------------------------------
# 🧠 Advanced Python Functions Examples
# ---------------------------------------

# 1. Using *args for variable arguments
def sum_all(*args):
    return sum(args)

# 2. Using **kwargs for keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 3. Lambda Function Example
square = lambda x: x ** 2
multiply = lambda x, y: x * y

# 4. Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 5. Function with Type Hinting
def divide(x: float, y: float) -> float:
    if y == 0:
        return float('inf')
    return x / y

# 6. Using Built-in Modules
import math
import random
from statistics import mean, median

def stats_demo(data):
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Square root of first element:", math.sqrt(data[0]))

# Run examples
if __name__ == "__main__":
    print("Sum all:", sum_all(1, 2, 3, 4, 5))
    print_info(name="Ali", age=30)
    print("Square of 6:", square(6))
    print("Multiply 4*5:", multiply(4, 5))
    print("Factorial of 5:", factorial(5))
    print("Divide 10 by 2:", divide(10, 2))

    sample_data = [4, 5, 6, 7, 8, 10]
    stats_demo(sample_data)
