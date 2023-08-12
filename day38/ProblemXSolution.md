# Unique Paths II: Robot in a Grid with Obstacles

This repository contains a Python solution to the problem of finding the number of unique paths for a robot to traverse from the top-left corner to the bottom-right corner of a grid while avoiding obstacles.

## Problem Description

Given an `m x n` grid, where each cell is either empty (0) or contains an obstacle (1), a robot is initially placed at the top-left corner (0, 0) and is tasked with reaching the bottom-right corner `(m - 1, n - 1)`. The robot can only move either down or right at any point in time and cannot traverse through cells with obstacles.

The goal is to calculate the number of possible unique paths that the robot can take to reach the destination.

## Example

**Input:**
```
obstacleGrid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
```

**Output:**
```
2
```

Explanation: There is one obstacle in the middle of the 3x3 grid above. There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

## Solution

To solve this problem, we can use dynamic programming to keep track of the number of unique paths for each cell in the grid. We'll create a 2D DP array with the same dimensions as the grid. The DP array will store the number of paths to each cell.

The algorithm can be summarized as follows:

1. If the starting cell has an obstacle, return 0 as there's no way to reach the destination.
2. Initialize the DP array with zeros, and set the starting cell to 1 (there's one way to reach it).
3. Iterate through each cell in the grid:
   - If the cell has an obstacle, set the corresponding DP cell to 0 (no paths).
   - If the cell doesn't have an obstacle, calculate the number of paths by adding the paths from the cells above and to the left.
4. The value in the bottom-right corner of the DP array will represent the total number of unique paths to the destination.

## Time Complexity

The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the grid. We need to iterate through each cell once to fill in the DP array.

## Space Complexity

The space complexity is O(m * n) as well, since we use a DP array of the same dimensions as the grid to store the number of paths for each cell. No additional space is used in the algorithm.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!