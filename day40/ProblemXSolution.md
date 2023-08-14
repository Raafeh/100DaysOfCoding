# Kth Largest Element in an Array

This repository contains a solution for finding the kth largest element in an integer array. The problem requires finding the kth largest element in the sorted order, not the kth distinct element.

## Problem Statement

Given an integer array `nums` and an integer `k`, the goal is to determine the kth largest element in the array.

### Examples

**Example 1:**
Input: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
Output: `5`

**Example 2:**
Input: `nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]`, `k = 4`
Output: `4`

## Approach and Solution

To solve this problem efficiently without explicitly sorting the entire array, we can use a min-heap. The following steps outline the approach:

1. Create an empty min-heap.

2. Iterate through the input array `nums`.

3. For each element in `nums`, add it to the min-heap using the `heapq.heappush()` method.

4. If the size of the heap becomes greater than `k`, remove the smallest element from the heap using the `heapq.heappop()` method. This ensures that we maintain a heap of the k largest elements encountered so far.

5. After iterating through all the elements, the heap will contain the k largest elements from the input array. The smallest element in the heap will be the kth largest element overall.

6. Return the smallest element in the heap, which is the kth largest element.

## Complexity Analysis

- Time Complexity: The time complexity of this solution is O(n * log(k)), where n is the number of elements in the `nums` array. This is because inserting and removing elements in/from the heap takes O(log(k)) time, and we perform this operation for each element in the array.
- Space Complexity: The space complexity is O(k), as we are maintaining a heap of size k to store the k largest elements.

