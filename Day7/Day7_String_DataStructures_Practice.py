
# ================================================
# Day 7 Python Practice Script: Strings & Data Structures
# From Easy to Intermediate with Explanations
# ================================================

print("\n========= STRING BASICS =========")

# Strip whitespace
a = "   Hello World!   "
print("Original:", repr(a))
print("Stripped:", a.strip())  # Removes leading/trailing spaces

# Change case
b = "Data SCIENCE"
print("Lowercase:", b.lower())
print("Uppercase:", b.upper())

# Replace content
text = "Python is cool"
print("Replace 'cool' with 'awesome':", text.replace("cool", "awesome"))

# Split string into list
fruits = "apple,banana,orange"
print("Split by comma:", fruits.split(","))

# Membership test
print("'apple' in fruits string:", "apple" in fruits)

# Escaping quotes
print("She said, \"Data Science rocks!\"")

# Tabs and newlines
print("Name:\tJohn\nRole:\tData Scientist")

# Raw string
print(r"Raw path: C:\Users\John\Docs")

print("\n========= STRING COMPARISON =========")

# Lexicographic comparison
print("abc" < "bcd")  # True
print("abc" == "abc")  # True
print("Zebra" > "apple")  # False because 'Z' < 'a' in Unicode

# Unicode values
print("ord('a') =", ord('a'))  # 97
print("ord('Z') =", ord('Z'))  # 90

print("\n========= LISTS =========")

L = [10, "apple", 3.5]
print("Original list:", L)

# Access and modify
print("L[1]:", L[1])
L[2] = "banana"
print("Modified list:", L)

# Append and delete
L.append("grape")
print("After append:", L)
del L[0]
print("After delete:", L)

# Copy list
L2 = L.copy()
print("Copied list:", L2)

print("\n========= TUPLES =========")

T = (1, "orange", 4.6)
print("Original tuple:", T)
print("T[1]:", T[1])

# Tuples are immutable
T2 = T + ("banana",)
print("Concatenated tuple:", T2)

T3 = T
print("Copied tuple:", T3)

print("\n========= SETS =========")

S = {1, "apple", 4.5}
print("Original set:", S)

# Add, update, remove
S.add("banana")
print("After add:", S)

S.update(["grape", 10])
print("After update:", S)

S.remove("apple")
print("After remove:", S)

S2 = S.copy()
print("Copied set:", S2)

print("\n========= DICTIONARIES =========")

D = {"name": "John", "age": 30}
print("Original dictionary:", D)

# Access and update
print("D['name']:", D["name"])
D["age"] = 31
D["role"] = "Engineer"
print("Updated dictionary:", D)

# Delete and copy
del D["name"]
print("After deletion:", D)

D2 = D.copy()
print("Copied dictionary:", D2)
