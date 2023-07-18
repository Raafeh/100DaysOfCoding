# Search Insert Position

## Problem Description

The problem is to find the index of a target value in a sorted array of distinct integers. If the target value is not found in the array, the algorithm should return the index where it would be inserted to maintain the sorted order. The algorithm needs to have a runtime complexity of O(log n).

## Example

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Approach and Solution

To solve the problem efficiently, we can use the binary search algorithm. The binary search algorithm works by repeatedly dividing the search space in half, reducing the search range until the target value is found or the search space is exhausted.

The provided solution is implemented as follows:

1. Initialize two pointers, `left` and `right`, to the start and end indices of the array, respectively.
2. Enter a while loop that continues as long as `left` is less than or equal to `right`.
3. Calculate the middle index `mid` as the average of `left` and `right`, rounded down to the nearest integer.
4. Check if the value at the middle index `mid` is equal to the target value. If it is, return `mid` as the index where the target is found.
5. If the value at `mid` is less than the target, update `left` to `mid + 1`, since the target value must be in the right half of the remaining array.
6. If the value at `mid` is greater than the target, update `right` to `mid - 1`, since the target value must be in the left half of the remaining array.
7. If the loop exits without finding the target, it means the target value is not present in the array. In this case, return `left` as the index where the target would be inserted to maintain the sorted order.

The time complexity of the solution is O(log n) because the binary search algorithm divides the search space in half at each iteration, resulting in a logarithmic time complexity.

The space complexity of the solution is O(1) because it uses a constant amount of additional space for the pointers and variables.

Overall, the provided solution is an efficient implementation that solves the problem with a logarithmic runtime complexity and a constant space complexity.