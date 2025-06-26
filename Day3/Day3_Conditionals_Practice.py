"""
Day 3 Practice: Conditional Statements in Python
Author: MichelleNiaa
Date: [Replace with current date]

This file includes multiple exercises for practicing:
- if, elif, else statements
- nested if conditions
- input type casting
- modulus for even/odd checks
- comparison logic
"""

# --------------------------
# Exercise 1: Largest of Three Numbers
# --------------------------
print("Exercise 1: Find the largest of three numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check which is greatest
if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

print("-" * 40)

# --------------------------
# Exercise 2: Even or Odd (Integer portion of float)
# --------------------------
print("Exercise 2: Integer portion and even/odd check")

x = float(input("Enter a floating point number: "))
y = round(x)

# Extracting integer part manually
if x > 0:
    intportion = y if y <= x else y - 1
else:
    intportion = y if y >= x else y + 1

print("Rounded value:", y)
print("Integer portion:", intportion)

# Check if integer portion is even or odd
if intportion % 2 == 0:
    print("It's EVEN.")
else:
    print("It's ODD.")

print("-" * 40)

# --------------------------
# Exercise 3: Driving Eligibility (Nested if)
# --------------------------
print("Exercise 3: Driving Eligibility")

age = int(input("Enter your age: "))

if age >= 18:
    experience = int(input("Enter years of driving experience: "))
    if experience >= 2:
        print("✅ Eligible for full license.")
    else:
        print("🛑 Not enough experience.")
else:
    print("🛑 Too young to drive.")

print("-" * 40)

# --------------------------
# Exercise 4: Score Grade (Multiple elifs)
# --------------------------
print("Exercise 4: Grade Evaluation")

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

print("-" * 40)

# --------------------------
# Exercise 5: Number Nature (Advanced Nested Conditions)
# --------------------------
print("Exercise 5: Number Nature Check")

num = float(input("Enter any number: "))

if num > 0:
    if num % 1 == 0:
        print("Positive Integer")
        if int(num) % 2 == 0:
            print("Even Integer")
        else:
            print("Odd Integer")
    else:
        print("Positive Decimal")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

print("-" * 40)
