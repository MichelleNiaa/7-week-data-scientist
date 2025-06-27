
"""
Day 4 - Python Practice: Control Flow, Loops, Conditionals, and List Operations
Author: [Your Name]
Date: [YYYY-MM-DD]
Description: This script includes advanced exercises covering:
- Loop control (break, continue, pass)
- Conditional logic
- List traversal and modification
- Sorting and indexing
"""

# Task 1: Find the minimum value and its index in a list
L = [1, 2, 4, -5, 7, 9, 3, 2]
m = L[0]  # Assume first element is the smallest initially
idx = 0   # To store index of minimum
c = 0     # Counter to track current index

for i in L:
    if i < m:
        m = i
        idx = c
    c += 1

print("Minimum value:", m)
print("Index of minimum value:", idx)

# Task 2: Sort the list without using sort() or sorted()
# Explanation: We'll use Selection Sort manually for learning purposes
unsorted_list = [6, 2, 9, 1, 4]
sorted_list = []

while unsorted_list:
    smallest = unsorted_list[0]
    for item in unsorted_list:
        if item < smallest:
            smallest = item
    sorted_list.append(smallest)
    unsorted_list.remove(smallest)

print("Manually sorted list:", sorted_list)

# Task 3: Loop with break and continue
i = 1
while True:
    if i % 17 == 0:
        print("Found a number divisible by 17:", i)
        break  # Exit the loop once found
    else:
        i += 1
        continue  # Skip the rest and go to next iteration

# Task 4: Loop over a mixed-type list and stop after a certain count
s = ["apple", 4.9, "cherry"]
i = 1
for x in s:
    print("Element:", x)
    i += 1
    if i == 3:
        break
else:
    print("Loop terminates with success")  # This will not print due to break

print("Outside the loop")

# Task 5: Custom function with type checking
def printMessage(msg):
    if isinstance(msg, str):
        print("Message:", msg)
    else:
        print("Input is not a string. Actual type:", type(msg))

# Call examples
printMessage("Hello, data science!")
printMessage(123)  # Will trigger error handling

# Task 6: Challenge - Build a sorted list from input and display stats
nums = [int(n) for n in input("Enter 5 numbers separated by spaces: ").split()]
sorted_nums = sorted(nums)
print("Sorted numbers:", sorted_nums)
print("Min:", sorted_nums[0], "| Max:", sorted_nums[-1], "| Mean:", sum(sorted_nums)/len(sorted_nums))
