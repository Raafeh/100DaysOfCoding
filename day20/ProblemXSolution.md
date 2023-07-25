# Peak Index in a Mountain Array 

## Problem Description

Given an array `arr` that represents a mountain, find the index `i` where `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`. In other words, find the index of the peak element in the mountain array.

**Input**
- The input array `arr` is guaranteed to be a mountain array.
- The length of the array `arr` will be at least 3.

**Output**
- Return the index `i` of the peak element.

## Example

Input: `arr = [0, 1, 0]`
Output: `1`
Explanation: The peak element is `1`, and its index is `1`.

Input: `arr = [0, 2, 1, 0]`
Output: `1`
Explanation: The peak element is `2`, and its index is `1`.

Input: `arr = [0, 10, 5, 2]`
Output: `1`
Explanation: The peak element is `10`, and its index is `1`.

## Solution

To solve this problem efficiently, we use a binary search algorithm. The binary search approach is chosen because the time complexity needs to be O(log(arr.length)), which means we need to minimize the number of iterations while searching for the peak element.

The binary search algorithm works as follows:

1. Initialize `left` and `right` pointers to the start and end of the array, respectively.
2. While `left` is less than `right`, do the following:
   a. Calculate the `mid` index as `left + (right - left) // 2`.
   b. Compare `arr[mid]` with `arr[mid + 1]`.
   c. If `arr[mid] < arr[mid + 1]`, it means we are on the ascending part of the mountain. So, the peak must be to the right of `mid`. Update `left = mid + 1`.
   d. If `arr[mid] >= arr[mid + 1]`, it means we are on the descending part of the mountain. So, the peak must be to the left of `mid` or could be the mid element itself. Update `right = mid`.
3. At the end of the binary search, `left` (or `right`) will point to the peak element in the mountain array. Return this index.

## Time Complexity

The time complexity of the binary search approach is O(log(arr.length)) since at each step, we reduce the search range by half.

## Space Complexity

The space complexity of the solution is O(1) as we are using only a few extra variables to perform the binary search, and the space does not depend on the input array size.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!