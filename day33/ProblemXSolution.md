# Search a 2D Matrix

## Problem Description

You are given an m x n integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, you need to implement a function to return `True` if the `target` is present in the matrix, or `False` otherwise.

## Example

**Input:**
```
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
```

**Output:**
```
True
```

**Input:**
```
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13
```

**Output:**
```
False
```

## Solution

To efficiently solve this problem in O(log(m * n)) time complexity, we can use a modified binary search algorithm. The key observation here is that the matrix has two essential properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Based on these properties, we can treat the matrix as a flattened sorted array and perform binary search on it. The goal of the binary search is to find the target element within the matrix efficiently.

The binary search algorithm works as follows:

1. Initialize two pointers, `left` and `right`, to the first and last elements of the flattened matrix.
2. While `left` is less than or equal to `right`, repeat the following steps:
    a. Calculate the `mid` index as `(left + right) // 2`.
    b. Retrieve the value of the element at the `mid` index in the flattened matrix.
    c. If the `mid_value` is equal to the `target`, return `True` as the target is found.
    d. If the `mid_value` is less than the `target`, set `left` to `mid + 1` to search the right half of the matrix.
    e. If the `mid_value` is greater than the `target`, set `right` to `mid - 1` to search the left half of the matrix.
3. If the loop terminates without finding the target, return `False`.

## Time Complexity

The time complexity of the provided solution is O(log(m * n)), where `m` is the number of rows and `n` is the number of columns in the matrix. This efficient time complexity is achieved through the binary search algorithm, allowing us to find the target element in the flattened matrix with fewer comparisons.

## Space Complexity

The space complexity of the code is O(1) since we are only using a constant amount of extra space to store the pointers `left`, `right`, and `mid`, without any dependency on the size of the input matrix.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!