
# beginner_functions.py
# ---------------------------------------
# 📘 Python Function Basics with Examples
# ---------------------------------------

# 1. Basic Function Definition
def greet():
    print("Hello, world!")

# 2. Function with Parameters
def add(x, y):
    return x + y

# 3. Function with Default Argument
def greet_user(name="Guest"):
    print(f"Welcome, {name}")

# 4. Function Returning a Value
def square(num):
    return num ** 2

# 5. Function with Conditional Logic
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# 6. Function Calling Another Function
def double_and_check(num):
    result = square(num)
    return check_even(result)

# Run examples
if __name__ == "__main__":
    greet()
    print("Add 3 + 4:", add(3, 4))
    greet_user()
    greet_user("Mahnaz")
    print("Square of 5:", square(5))
    print("Is 8 even?:", check_even(8))
    print("Double and check for 3:", double_and_check(3))
