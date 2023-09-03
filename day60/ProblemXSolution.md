# Unique Paths

## Problem Description

You are given a robot that is initially located at the top-left corner of an `m x n` grid. The robot's task is to move to the bottom-right corner of the grid, and it can only move either down or right at any point in time. Your goal is to find the number of possible unique paths that the robot can take to reach the destination.

### Example

**Input:**
```
m = 3, n = 7
```

**Output:**
```
28
```

In this example, the robot needs to move from the top-left corner to the bottom-right corner in a grid with 3 rows and 7 columns. There are 28 unique paths the robot can take to reach its destination.

## Approach and Solution

To solve this problem efficiently, we can use dynamic programming. We'll create a 2D array, `dp`, of size `m x n`, where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)` from the top-left corner `(0, 0)`.

We start by initializing all values in `dp` to 1 since there is always only one way to reach any cell in the first row and the first column (by moving either right or down).

Then, we iterate through the grid, starting from `(1, 1)` to `(m-1, n-1)`. For each cell `(i, j)`, we calculate the number of unique paths to it by summing up the paths from above `(i-1, j)` and from the left `(i, j-1)` cells.

Finally, the result is stored in `dp[m-1][n-1]`, which represents the total number of unique paths from the top-left corner to the bottom-right corner.

### Time Complexity

The time complexity of this solution is O(m * n) because we iterate through the entire `m x n` grid once to fill in the `dp` array.

### Space Complexity

The space complexity is also O(m * n) because we create a 2D `dp` array of the same size as the input grid to store intermediate results.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!