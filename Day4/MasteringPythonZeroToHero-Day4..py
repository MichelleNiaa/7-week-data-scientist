
# Python Program to find the index and value of the smallest number in a list,
# and then create a sorted version of the list (ascending order)

# Original list of integers
L = [1, 2, 4, -5, 7, 9, 3, 2]

# Step 1: Initialize the minimum value (m) as the first element of the list
m = L[0]

# Step 2: Initialize an index tracker (idx) to store the position of the minimum value
idx = 0

# Step 3: Initialize a counter (c) to track the current index while iterating
c = 0

# Step 4: Iterate over the list to find the minimum value and its index
for i in L:
    if i < m:          # If current element is smaller than current minimum
        m = i          # Update minimum value
        idx = c        # Update index of the minimum value
    c += 1             # Move to next index

# Step 5: Output the index and value of the smallest number
print("Index of minimum value:", idx)
print("Minimum value:", m)

# Now sort the list in ascending order using Python's built-in sorted() function
sorted_list = sorted(L)

# Step 6: Output the sorted list
print("Sorted List (Ascending Order):", sorted_list)
