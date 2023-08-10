# Search in Rotated Sorted Array II


## Problem Description

Given a sorted integer array that has been rotated at an unknown pivot index, we need to find whether a given target value exists in the array.

For example:
- Input: `nums = [2, 5, 6, 0, 0, 1, 2]`, `target = 0`
  Output: `True`
  
- Input: `nums = [2, 5, 6, 0, 0, 1, 2]`, `target = 3`
  Output: `False`

## Approach and Solution

The provided solution uses a binary search algorithm to efficiently search for the target value in the rotated sorted array. The key idea is to adjust the binary search to consider the rotation while narrowing down the search range.

1. Initialize two pointers, `lo` and `hi`, to define the current search range.

2. While `lo` is less than or equal to `hi`:

   a. Calculate the middle index `mid = (lo + hi) // 2`.

   b. If `nums[mid]` is equal to the `target`, return `True`.

   c. If `nums[lo] == nums[mid]`, increment `lo` by 1 to skip duplicate elements.

   d. If the subarray from `lo` to `mid` is sorted (i.e., `nums[lo] <= nums[mid]`):

      - If `nums[lo] <= target < nums[mid]`, update `hi = mid - 1`.
      - Otherwise, update `lo = mid + 1`.

   e. If the subarray from `mid` to `hi` is sorted (i.e., `nums[mid] <= nums[hi]`):

      - If `nums[mid] < target <= nums[hi]`, update `lo = mid + 1`.
      - Otherwise, update `hi = mid - 1`.

3. If the target is not found after the loop, return `False`.

## Time Complexity

The provided solution has a time complexity of O(log N), where N is the number of elements in the input array. This is because the binary search algorithm reduces the search space by half in each step.

## Space Complexity

The solution has a space complexity of O(1), as it only uses a constant amount of extra space to store variables regardless of the input size.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!