# 01 Matrix Problem

## Problem Description

Given an m x n binary matrix `mat`, where `mat[i][j]` is either 0 or 1, the task is to calculate the distance of the nearest 0 for each cell and return the resulting matrix.

### Example

**Input:**
```
mat = [[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]]
```

**Output:**
```
result = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]
```

**Input:**
```
mat = [[0, 0, 0],
       [0, 1, 0],
       [1, 1, 1]]
```

**Output:**
```
result = [[0, 0, 0],
          [0, 1, 0],
          [1, 2, 1]]
```

## Approach and Solution 

The problem can be efficiently solved using the Breadth-First Search (BFS) algorithm. Here's the step-by-step explanation of the solution approach:

1. Create a `queue` to hold the positions of cells to be visited during BFS traversal.
2. Create a `distance` matrix to store the calculated distances of each cell from the nearest 0.
3. Initialize the `queue` with the positions of all cells containing 0 in the input matrix and set their corresponding distances in the `distance` matrix to 0.
4. Start a BFS traversal from the cells with value 0. For each cell visited, explore its neighboring cells (up, down, left, and right).
5. Update the distance of each neighboring cell if the distance from the current cell plus 1 is smaller than its current distance.
6. Continue the BFS traversal until the queue is empty.
7. Return the `distance` matrix as the result.

### Time Complexity

The BFS traversal visits each cell once, and for each cell, it examines its neighboring cells. In the worst case, each cell might be visited multiple times due to the wave-like traversal pattern. Therefore, the time complexity of the solution is O(m * n), where m is the number of rows and n is the number of columns in the input matrix.

### Space Complexity

The additional space used in the solution includes the `queue`, the `distance` matrix, and the `directions` list. The space complexity is O(m * n) to store the `distance` matrix and O(min(m, n)) for the `queue` and `directions` list.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!