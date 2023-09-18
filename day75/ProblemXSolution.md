# K Weakest Rows in a Binary Matrix

## Problem Description

You are given an `m x n` binary matrix `mat` consisting of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row `i` is weaker than a row `j` if one of the following is true:

1. The number of soldiers in row `i` is less than the number of soldiers in row `j`.
2. Both rows have the same number of soldiers, and `i` < `j`.

You need to find and return the indices of the `k` weakest rows in the matrix ordered from weakest to strongest.

### Example

**Input:**
```python
mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
```

**Output:**
```python
[2, 0, 3]
```

**Explanation:**
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2, 0, 3, 1, 4].

## Approach and Solution

To solve this problem, we can follow these steps:

1. Create a list of tuples where each tuple contains two elements: the sum of soldiers in the row and the index of the row.
2. Sort the list of tuples based on the sum of soldiers in ascending order.
3. Extract the indices of the `k` weakest rows from the sorted list of tuples.


### Time and Space Complexity

The time complexity of this solution is dominated by the sorting step, which has a time complexity of O(m * log(m)), where `m` is the number of rows in the matrix.

The space complexity is O(m), where `m` is the number of rows in the matrix, as we create a list of tuples to store the sum of soldiers and row indices.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
