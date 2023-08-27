# Minimum Depth of Binary Tree

This repository contains a solution to the problem of finding the minimum depth of a binary tree. The minimum depth is defined as the number of nodes along the shortest path from the root node down to the nearest leaf node.

## Problem Description

Given a binary tree, the task is to find its minimum depth. A leaf node is a node with no children.

## Approach and Solution

To solve the problem, I used Depth-First Search (DFS) approach to traverse the binary tree. The algorithm follows these steps:

1. If the root node is null, the minimum depth is 0 (the tree has no nodes).
2. If both the left and right child of the root node are null, the minimum depth is 1 (the tree has only one node, which is the root).
3. If the left child is null, recursively calculate the minimum depth of the right subtree and add 1 to it. Return this value as the minimum depth.
4. If the right child is null, recursively calculate the minimum depth of the left subtree and add 1 to it. Return this value as the minimum depth.
5. If both the left and right children are not null, recursively calculate the minimum depth of both the left and right subtrees. Take the minimum of the two depths and add 1 to it. Return this value as the minimum depth.

The time complexity of this approach is O(n), where n is the number of nodes in the binary tree. This is because we need to visit each node once during the DFS traversal.

The space complexity is O(h), where h is the height of the binary tree. In the worst case, the height of the binary tree can be equal to the number of nodes, resulting in O(n) space complexity. However, in a balanced binary tree, the height is logarithmic to the number of nodes, resulting in O(log n) space complexity.

Feel free to explore the provided code implementation and modify it to suit your needs. Happy coding!
