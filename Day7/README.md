# 📘 Day 7 – Python Fundamentals: Strings, Escape Characters & Data Structures

Welcome to Day 7 of my 7-week Data Science Learning Challenge!  
Today focused on two major areas:

1. 🔤 Mastering Python **String operations**  
2. 📦 Understanding core **Python Data Structures**: `list`, `tuple`, `set`, and `dictionary`

---

## 🔹 1. String Manipulation & Escape Characters

### ✅ Topics Covered:
- Removing whitespace with `.strip()`
- Changing case with `.lower()` and `.upper()`
- Replacing text with `.replace()`
- Splitting strings into lists with `.split()`
- Checking substrings using `in` and `not in`
- Escaping quotes (`\"`, `\'`)
- Special characters like `\t` (tab) and `\n` (newline)
- Using raw strings (`r"..."`) for file paths

### 💻 Example Code:
```python
a = "   Hello World!   "
b = a.strip()
print(b.lower())      # hello world!
print(b.upper())      # HELLO WORLD!
print(a.replace(" ", "_"))  # ___Hello_World!___

sentence = "game,and,no"
L = sentence.split(",")  # ['game', 'and', 'no']
print("and" in sentence)  # True

# Escape characters
print("He said \"Python is great!\"")
print('It\'s a great day!')
print("Path: C:\\Users\\Name")
print(r"Raw path: C:\Users\Name")

# Special characters
print("line1\nline2")  # newline
print("word1\tword2")  # tab
