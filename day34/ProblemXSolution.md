# Rotated Sorted Array Search

## Problem Statement

You are given an integer array `nums` that is sorted in ascending order with distinct values. The array has been rotated at an unknown pivot index `k` (1 <= k < nums.length), resulting in a rotated sorted array. Your task is to find the index of the target element in the array, or return -1 if the target is not present.

**Example:**

Input: `nums = [4,5,6,7,0,1,2]`, `target = 0`
Output: `4`

Input: `nums = [4,5,6,7,0,1,2]`, `target = 3`
Output: `-1`

## Approach and Solution

The key idea is to determine the pivot point where the array has been rotated. After finding the pivot, the algorithm performs two separate binary searches on the segments of the array before and after the pivot.

1. If the array is not rotated, perform a regular binary search on the entire array.
2. If the array is rotated, calculate the pivot and perform binary searches on the appropriate segments.

The solution includes the following components:

1. A `binarySearch` function that performs a standard binary search to find the target element's index within a specified range.
2. A `findPivot` function that calculates the pivot index where the array has been rotated.
3. The main `search` function that determines whether the array is rotated or not and then performs the appropriate binary searches.

**Time Complexity:** O(log n)
The solution utilizes binary search techniques, which have a logarithmic runtime complexity. The search operations on the rotated array segments take place within a logarithmic number of steps, leading to an overall time complexity of O(log n).

**Space Complexity:** O(1)
The solution uses a constant amount of additional space for variables and indices, resulting in a space complexity of O(1).

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!