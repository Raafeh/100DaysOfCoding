# Path with Minimum Effort

## Problem Description

Given a 2D grid `heights`, where `heights[row][col]` represents the height of cell `(row, col)`, the task is to find the minimum effort required to travel from the top-left cell `(0, 0)` to the bottom-right cell `(rows-1, columns-1)`.

### Example

**Input:**
```
heights = [[1,2,2],[3,8,2],[5,3,5]]
```

**Output:**
```
2
```

**Explanation:**
The route of `[1,3,5,3,5]` has a maximum absolute difference of 2 in consecutive cells, which is the minimum effort.

## Approach and Solution

The solution to this problem involves a combination of binary search and breadth-first search (BFS). The main idea is to perform a binary search on the range of possible efforts and use BFS to check if there exists a path from the top-left cell to the bottom-right cell with a maximum absolute difference in heights less than or equal to the current binary search value.

Here's how the algorithm works:

1. Initialize a binary search range between 0 and a large value (e.g., 10^6).

2. Define a helper function `isPathPossible(maxEffort)` that uses BFS to check if a path is possible with a given maximum effort. It starts from the top-left cell and explores neighboring cells while ensuring that the absolute difference in heights does not exceed `maxEffort`.

3. Perform binary search within the defined range. For each iteration of the binary search, call the `isPathPossible` function. If it returns `True`, narrow down the search range to the left half; otherwise, narrow it down to the right half.

4. Continue the binary search until the left and right pointers meet, and return the final value of `left` as the minimum effort.


- Time Complexity: O(rows * cols * log(MAX)), where `rows` and `cols` are the dimensions of the input grid, and `MAX` represents the maximum possible difference in heights. The binary search has a time complexity of O(log(MAX)), and for each binary search iteration, the BFS takes O(rows * cols) time in the worst case.

- Space Complexity: O(rows * cols) for the visited matrix used in BFS, where `rows` and `cols` are the dimensions of the input grid.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
