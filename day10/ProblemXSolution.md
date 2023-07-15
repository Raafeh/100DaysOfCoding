# Check if Array is Sorted and Rotated

## Problem Description
Given an array `nums`, the task is to determine if the array was originally sorted in non-decreasing order and then rotated some number of positions (including zero). The array may contain duplicates.

An array `A` is considered rotated by `x` positions if `A[i] == B[(i + x) % A.length]`, where `%` denotes the modulo operation.

The task is to implement a function `check(nums: List[int]) -> bool` that takes in the `nums` array and returns `True` if the array satisfies the conditions of being sorted and rotated, and `False` otherwise.

## Approach and Solution
To solve this problem, we can iterate through the array and compare each element with the next element (taking modulo `n` to handle the wrap-around). If an element is greater than its next element, it means the array is not sorted in non-decreasing order. We keep track of the count of such occurrences.

If the count exceeds 1, it means the array was rotated more than once, which violates the conditions of the problem. In that case, we return `False`.

If we finish iterating through the array without encountering more than one out-of-order element, it means the array was originally sorted in non-decreasing order and then rotated. In that case, we return `True`.

The time complexity of this approach is O(n), where n is the length of the input array `nums`. This is because we iterate through the entire array once.

The space complexity of this approach is O(1) because we only use a constant amount of extra space to store the count variable.

Feel free to explore the provided code implementation and modify it to suit your needs. Happy coding!