# All Possible Full Binary Trees

This GitHub repository contains a solution to the problem of generating all possible full binary trees with a given number of nodes (n), where each node has a value of 0. The problem statement specifies that a full binary tree is a binary tree where each node has exactly 0 or 2 children.

## Problem Description

Given an integer n, the task is to generate a list of all possible full binary trees with n nodes, where each node's value is 0. The output should contain the root nodes of all the valid full binary trees. Each element of the output list represents the root node of one possible tree.

### Example 1:

Input: n = 7

Output:
```
[
  [0,0,0,null,null,0,0,null,null,0,0],
  [0,0,0,null,null,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,null,null,null,null,0,0],
  [0,0,0,0,0,null,null,0,0]
]
```

### Example 2:

Input: n = 3

Output:
```
[[0,0,0]]
```

## Approach and Solution

To solve the problem, we utilize a recursive approach to generate all the possible full binary trees with the given constraints. We define a class `Solution` with the method `allPossibleFBT`, which takes an integer `n` as input and returns the list of possible full binary trees.

### Recursive Algorithm:

1. The base case for the recursion is when n is less than or equal to 0 or when n is even. In such cases, we cannot form a full binary tree, so we return an empty list.

2. If n is equal to 1, we have a single node in the tree, and we return a list containing the root node with value 0.

3. For odd values of n greater than 1, we proceed with the recursive approach:
   - We iterate through all possible combinations of left and right subtrees by dividing n into left and right subtree sizes.
   - For each left subtree size `i` (ranging from 1 to n-2 with a step of 2), we generate all possible left subtrees.
   - For each right subtree size `n-i-1`, we generate all possible right subtrees.
   - We then combine the left and right subtrees to form new full binary trees with the root node having value 0.
   - We add all the newly formed trees to the result list.

4. Finally, we return the list of all possible full binary trees with n nodes.

### Time Complexity

The time complexity of the solution can be analyzed in terms of the number of recursive function calls made and the work done in each call. Since each recursive call reduces the value of n to half (approximately), the time complexity can be expressed as O(2^n), where n is the input integer.

### Space Complexity

The space complexity is determined by the recursive stack used during the function calls. For each call, a new set of left and right subtrees is generated, and the maximum depth of the recursion is proportional to n. Hence, the space complexity of the solution is O(n).

Overall, the solution efficiently generates all possible full binary trees with node values equal to 0 using a recursive approach, making it a viable solution for small values of n. However, for large values of n, the time complexity grows exponentially, and the computation might become impractical.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!