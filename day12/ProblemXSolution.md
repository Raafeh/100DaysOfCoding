# Add Two Numbers II

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first, and each of their nodes contains a single digit. Your task is to add the two numbers and return the sum as a linked list.

## Example

<img src="https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg" alt="Binary Tree" width="500" height="250">

**Input:**

```
l1 = [7,2,4,3]
l2 = [5,6,4]
```

**Output:**

```
[7,8,0,7]
```

## Approach and Solution 

To solve this problem, we can use the following approach:

1. Reverse the order of digits in the input linked lists using stacks.
2. Traverse both reversed lists simultaneously, performing digit-wise addition and keeping track of the carry.
3. Create a new linked list to store the result, with the most significant digit at the beginning.
4. Return the head of the resulting linked list.

The time and space complexity of this solution is O(max(N, M)), where N and M are the lengths of the two input linked lists.

