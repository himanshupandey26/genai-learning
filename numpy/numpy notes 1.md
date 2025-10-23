# NumPy Beginner's Guide with Detailed Examples

I'll provide a comprehensive NumPy tutorial with code, outputs, and detailed comments.

## 1. Introduction and Installation

```python
# NumPy is the fundamental package for scientific computing in Python
# It provides support for large, multi-dimensional arrays and matrices

import numpy as np

# Check NumPy version
print("NumPy version:", np.__version__)
```
**Output:**
```
NumPy version: 1.24.3
```

---

## 2. Creating Arrays

```python
# Creating arrays from Python lists
# 1D Array (Vector)
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("Type:", type(arr1))
print("Data type:", arr1.dtype)
print()

# 2D Array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print("Shape:", arr2.shape)  # (rows, columns)
print("Dimensions:", arr2.ndim)
print("Size (total elements):", arr2.size)
```
**Output:**
```
1D Array: [1 2 3 4 5]
Type: <class 'numpy.ndarray'>
Data type: int64

2D Array:
 [[1 2 3]
 [4 5 6]]
Shape: (2, 3)
Dimensions: 2
Size (total elements): 6
```

---

## 3. Array Creation Functions

```python
# Creating arrays with built-in functions

# Array of zeros
zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print("Zeros array:\n", zeros)
print()

# Array of ones
ones = np.ones((2, 3))
print("Ones array:\n", ones)
print()

# Array with a specific value
full = np.full((2, 2), 7)
print("Full array (filled with 7):\n", full)
print()

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix
print("Identity matrix:\n", identity)
print()

# Array with a range of values
range_arr = np.arange(0, 10, 2)  # start, stop, step
print("Range array:", range_arr)
print()

# Linearly spaced array
linspace = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("Linearly spaced:", linspace)
print()

# Random arrays
random_arr = np.random.random((2, 3))  # values between 0 and 1
print("Random array:\n", random_arr)
print()

# Random integers
random_int = np.random.randint(1, 100, size=(3, 3))  # integers from 1 to 99
print("Random integers:\n", random_int)
```
**Output:**
```
Zeros array:
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

Ones array:
 [[1. 1. 1.]
 [1. 1. 1.]]

Full array (filled with 7):
 [[7 7]
 [7 7]]

Identity matrix:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Range array: [0 2 4 6 8]

Linearly spaced: [0.   0.25 0.5  0.75 1.  ]

Random array:
 [[0.5488135  0.71518937 0.60276338]
 [0.54488318 0.4236548  0.64589411]]

Random integers:
 [[43 92 77]
 [60 80 96]
 [33 71 86]]
```

---

## 4. Array Indexing and Slicing

```python
# Creating a sample array
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original array:", arr)

# Indexing (accessing single elements)
print("First element:", arr[0])
print("Last element:", arr[-1])
print()

# Slicing (accessing multiple elements)
print("Elements from index 1 to 4:", arr[1:4])  # excludes index 4
print("First 3 elements:", arr[:3])
print("Last 3 elements:", arr[-3:])
print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])
print()

# 2D array indexing
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
print("2D Array:\n", arr2d)
print("Element at row 1, column 2:", arr2d[1, 2])
print("First row:", arr2d[0, :])
print("Second column:", arr2d[:, 1])
print("Subarray (rows 0-1, columns 1-3):\n", arr2d[0:2, 1:3])
```
**Output:**
```
Original array: [10 20 30 40 50 60]
First element: 10
Last element: 60

Elements from index 1 to 4: [20 30 40]
First 3 elements: [10 20 30]
Last 3 elements: [40 50 60]
Every second element: [10 30 50]
Reverse array: [60 50 40 30 20 10]

2D Array:
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Element at row 1, column 2: 7
First row: [1 2 3 4]
Second column: [ 2  6 10]
Subarray (rows 0-1, columns 1-3):
 [[2 3]
 [6 7]]
```

---

## 5. Array Operations (Element-wise)

```python
# Basic arithmetic operations
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Array a:", a)
print("Array b:", b)
print()

# Element-wise operations
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Power (a ** 2):", a ** 2)
print("Square root:", np.sqrt(a))
print()

# Operations with scalars (broadcasting)
print("a + 10:", a + 10)
print("a * 3:", a * 3)
```
**Output:**
```
Array a: [1 2 3 4]
Array b: [10 20 30 40]

Addition (a + b): [11 22 33 44]
Subtraction (a - b): [-9 -18 -27 -36]
Multiplication (a * b): [ 10  40  90 160]
Division (a / b): [0.1 0.1 0.1 0.1]
Power (a ** 2): [ 1  4  9 16]
Square root: [1.         1.41421356 1.73205081 2.        ]

a + 10: [11 12 13 14]
a * 3: [ 3  6  9 12]
```

---

## 6. Statistical Operations

```python
# Creating sample data
data = np.array([10, 20, 30, 40, 50])
print("Data:", data)
print()

# Statistical functions
print("Sum:", np.sum(data))
print("Mean (average):", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", np.std(data))
print("Variance:", np.var(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Index of minimum:", np.argmin(data))
print("Index of maximum:", np.argmax(data))
print()

# 2D array statistics
data2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D Data:\n", data2d)
print()
print("Total sum:", np.sum(data2d))
print("Sum along axis 0 (columns):", np.sum(data2d, axis=0))
print("Sum along axis 1 (rows):", np.sum(data2d, axis=1))
print("Mean of each column:", np.mean(data2d, axis=0))
```
**Output:**
```
Data: [10 20 30 40 50]

Sum: 150
Mean (average): 30.0
Median: 30.0
Standard deviation: 14.142135623730951
Variance: 200.0
Minimum: 10
Maximum: 50
Index of minimum: 0
Index of maximum: 4

2D Data:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

Total sum: 45
Sum along axis 0 (columns): [12 15 18]
Sum along axis 1 (rows): [ 6 15 24]
Mean of each column: [4. 5. 6.]
```

---

## 7. Reshaping Arrays

```python
# Creating a 1D array
arr = np.arange(12)
print("Original array:", arr)
print("Shape:", arr.shape)
print()

# Reshaping to 2D
reshaped = arr.reshape(3, 4)  # 3 rows, 4 columns
print("Reshaped to (3, 4):\n", reshaped)
print()

# Reshaping to 3D
reshaped3d = arr.reshape(2, 2, 3)
print("Reshaped to (2, 2, 3):\n", reshaped3d)
print()

# Flatten back to 1D
flattened = reshaped.flatten()
print("Flattened:", flattened)
print()

# Transpose (swap rows and columns)
print("Original:\n", reshaped)
print("\nTransposed:\n", reshaped.T)
```
**Output:**
```
Original array: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Shape: (12,)

Reshaped to (3, 4):
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Reshaped to (2, 2, 3):
 [[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]

Flattened: [ 0  1  2  3  4  5  6  7  8  9 10 11]

Original:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Transposed:
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
```

---

## 8. Boolean Indexing and Filtering

```python
# Creating sample data
arr = np.array([10, 25, 30, 15, 40, 5])
print("Array:", arr)
print()

# Boolean conditions
condition = arr > 20
print("Condition (arr > 20):", condition)
print("Elements greater than 20:", arr[condition])
print()

# Multiple conditions (use & for AND, | for OR)
condition2 = (arr > 10) & (arr < 40)
print("Elements between 10 and 40:", arr[condition2])
print()

# Using np.where (like ternary operator)
result = np.where(arr > 20, "High", "Low")
print("High/Low classification:", result)
print()

# Getting indices where condition is True
indices = np.where(arr > 20)
print("Indices where arr > 20:", indices[0])
```
**Output:**
```
Array: [10 25 30 15 40  5]

Condition (arr > 20): [False  True  True False  True False]
Elements greater than 20: [25 30 40]

Elements between 10 and 40: [25 30 15]

High/Low classification: ['Low' 'High' 'High' 'Low' 'High' 'Low']

Indices where arr > 20: [1 2 4]
```

---

## 9. Array Concatenation and Stacking

```python
# Creating sample arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)
print()

# Vertical stacking (stack rows)
vstack = np.vstack((arr1, arr2))
print("Vertical stack:\n", vstack)
print()

# Horizontal stacking (stack columns)
hstack = np.hstack((arr1, arr2))
print("Horizontal stack:\n", hstack)
print()

# Concatenate along specific axis
concat_axis0 = np.concatenate((arr1, arr2), axis=0)  # same as vstack
concat_axis1 = np.concatenate((arr1, arr2), axis=1)  # same as hstack
print("Concatenate axis=0:\n", concat_axis0)
print("\nConcatenate axis=1:\n", concat_axis1)
```
**Output:**
```
Array 1:
 [[1 2]
 [3 4]]

Array 2:
 [[5 6]
 [7 8]]

Vertical stack:
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]

Horizontal stack:
 [[1 2 5 6]
 [3 4 7 8]]

Concatenate axis=0:
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]

Concatenate axis=1:
 [[1 2 5 6]
 [3 4 7 8]]
```

---

## 10. Array Splitting

```python
# Creating a sample array
arr = np.arange(16).reshape(4, 4)
print("Original array:\n", arr)
print()

# Split horizontally (split columns)
h_split = np.hsplit(arr, 2)  # split into 2 equal parts
print("Horizontal split (2 parts):")
print("Part 1:\n", h_split[0])
print("Part 2:\n", h_split[1])
print()

# Split vertically (split rows)
v_split = np.vsplit(arr, 2)
print("Vertical split (2 parts):")
print("Part 1:\n", v_split[0])
print("Part 2:\n", v_split[1])
```
**Output:**
```
Original array:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

Horizontal split (2 parts):
Part 1:
 [[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]
Part 2:
 [[ 2  3]
 [ 6  7]
 [10 11