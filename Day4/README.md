# 📘 Day 4 – List Operations: Finding Minimum and Sorting

Welcome to Day 4 of the **"Mastering Python Zero to Hero"** journey!  
In this exercise, we dive deeper into **list manipulation**, including how to:

1. ✅ Find the **minimum value** in a list  
2. ✅ Track the **index** of that minimum value  
3. ✅ Generate a **sorted list** in ascending order  

---

## 🧠 Learning Objectives

- Understand how to iterate over a list using a loop.
- Apply conditional logic to track minimum values.
- Learn how to manage **index tracking** manually.
- Use the built-in `sorted()` function for sorting lists.
- Structure readable, commented Python code.

---

## 🧪 What This Program Does

The uploaded file `Day4_SortedList_Explained.py` contains a complete Python script that:

1. **Takes a list of integers**: `[1, 2, 4, -5, 7, 9, 3, 2]`
2. **Finds the smallest number** (`-5`) and its index (`3`)
3. **Sorts the list** into ascending order
4. **Prints** all the results with explanations

---

## 📜 Step-by-Step Breakdown

### 🔢 Step 1: Initialize Variables
```python
L = [1, 2, 4, -5, 7, 9, 3, 2]
m = L[0]
idx = 0
c = 0
