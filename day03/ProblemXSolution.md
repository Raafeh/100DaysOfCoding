# Subarray Sum Problem

## Problem Description
Given an unsorted array `A` of size `N` that contains only positive integers, the task is to find a continuous subarray whose elements add up to a given number `S`. You need to return the left and right indexes (1-based indexing) of that subarray. If multiple subarrays satisfy the condition, return the indexes of the subarray that appears first when moving from left to right.

## Example
**Input:**
```
A = [1, 4, 20, 3, 10, 5]
S = 33
```
**Output:**
```
[3, 5]
```
**Explanation:**
In the given array, the subarray [20, 3, 10] has a sum of 33. The left index is 3, and the right index is 5.

## Approach and Solution
To solve this problem, we can use the sliding window technique. We maintain two pointers, `left` and `right`, initially set to 0. We also keep track of the current sum of the subarray using the variable `current_sum`.

We start by moving the `right` pointer from left to right and adding the elements to `current_sum`. If `current_sum` becomes greater than the target sum `S`, we subtract the element at the `left` index from `current_sum` and increment `left` by 1. We continue this process until `current_sum` becomes less than or equal to `S`.

Whenever `current_sum` becomes equal to `S`, we have found a subarray that satisfies the condition. We return the left and right indexes of that subarray.

If no subarray is found, we return an empty list.

## Complexity Analysis
The time complexity of this approach is O(N) as we iterate through the array once.

The space complexity is O(1) since we only use a constant amount of additional space to store variables.

Feel free to explore the code and provide your feedback. Happy coding!
