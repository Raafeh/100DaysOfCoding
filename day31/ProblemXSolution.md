# Unique BSTs II

## Problem Description

Given an integer `n`, the task is to generate all structurally unique BSTs with exactly `n` nodes such that each node contains a unique value from 1 to `n`. Return the answer in any order.

## Example

**Input:** `n = 3`

**Output:**

```
[
    [1, None, 2, None, 3],
    [1, None, 3, 2],
    [2, 1, 3],
    [3, 1, None, None, 2],
    [3, 2, None, 1]
]
```

**Input:** `n = 1`

**Output:**

```
[[1]]
```

## Solution

To generate all structurally unique BSTs, we can use a recursive approach. The main idea is to consider each number from 1 to `n` as the root of the BST and recursively generate left and right subtrees. Then, combine them to form unique BSTs.

We define a helper function `generate_trees(start, end)` that generates all possible BSTs between the range `start` to `end`. If `start > end`, it returns a list with a single element - `None`, indicating an empty subtree.

The recursive algorithm works as follows:
1. Base case: If `start > end`, return `[None]` (empty subtree).
2. Initialize an empty list `all_trees`.
3. Iterate from `start` to `end`, denoting the root value as `i`.
4. Recursively call `generate_trees` for the left subtree with the range `start` to `i-1`, and for the right subtree with the range `i+1` to `end`.
5. Combine each left subtree with each right subtree for all possible combinations.
6. Create a new root node with the value `i` and set its left and right children to the left and right subtrees generated in the previous step.
7. Append the root node to the `all_trees` list.
8. Return the list `all_trees`.

The final result will be obtained by calling `generate_trees(1, n)`.


The time complexity of the solution is determined by the number of unique BSTs generated. For each value from 1 to `n`, we generate all possible combinations of left and right subtrees, resulting in `Catalan(n)` unique BSTs. Therefore, the time complexity is approximately O(Catalan(n)), which grows exponentially with `n`.

The space complexity is determined by the number of recursive calls on the call stack and the space required to store the unique BSTs. Since we generate all the unique BSTs, the space complexity is also O(Catalan(n)) in the worst case.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!