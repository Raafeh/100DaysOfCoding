# Shortest Bridge 

## Problem Statement

You are given a binary matrix where `1` represents land and `0` represents water. Your task is to find the smallest number of `0`s you must flip to connect the two islands in the matrix. An island is defined as a group of `1`s that are 4-directionally connected and not connected to any other `1`s. There are exactly two islands in the matrix.

### Example

**Input:**

```python
grid = [
    [0, 1],
    [1, 0]
]
```

**Output:**

```
1
```

**Input:**

```python
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1]
]
```

**Output:**

```
2
```

**Input:**

```python
grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
```

**Output:**

```
1
```

## Approach and Solution

To solve this problem, we can use a combination of Depth-First Search (DFS) and Breadth-First Search (BFS) to identify and connect the two islands.

#### DFS to Find Islands
1. We start by iterating through the binary matrix to find the first island. When we find a `1`, we perform a DFS to identify all the connected `1`s and mark them as `2` to avoid revisiting.

#### BFS to Find Shortest Path
2. After marking the first island, we use a BFS to find the shortest path to the second island. We start with the cells of the first island in a queue and move outward, marking cells as `2` to avoid revisiting.
3. When we encounter a cell containing `1`, we know that we have found the second island, and the distance to it is the minimum number of flips required.
4. The solution is the number of flips (i.e., the distance) required to connect the two islands.


- Time Complexity: The DFS and BFS both run in O(n^2), where n is the number of rows or columns in the binary matrix.

- Space Complexity: The space complexity for both the DFS and BFS is O(n^2) as well, as we use additional data structures to store visited cells and the queue for BFS.

