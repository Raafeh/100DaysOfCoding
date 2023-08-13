# Valid Subarray Partitioning

## Problem Description

Given a 0-indexed integer array `nums`, the task is to determine whether the array can be partitioned into one or more contiguous subarrays, with each subarray satisfying one of the following conditions:

1. The subarray consists of exactly 2 equal elements.
2. The subarray consists of exactly 3 equal elements.
3. The subarray consists of exactly 3 consecutive increasing elements, where the difference between adjacent elements is 1.

The goal is to return `True` if the array has at least one valid partition, and `False` otherwise.

### Example

**Input:**
```
nums = [4, 4, 4, 5, 6]
```

**Output:**
```
True
```

Explanation: The array can be partitioned into the subarrays [4, 4] and [4, 5, 6], both of which are valid according to the given conditions.

## Approach and Solution 

The provided solution employs a dynamic programming approach to solve the problem efficiently. The solution iterates through the array while maintaining a rolling window of validity statuses. Here's how the solution works:

1. Initialize three boolean values `dp` to keep track of the validity for each subarray type: 2 equal elements, 3 equal elements, and 3 consecutive increasing elements.
2. Iterate through the array starting from index 2:
   a. Calculate the current validity status based on the previous statuses and the current element's properties.
   b. Update the `dp` values with the current validity status and the rolling window approach.

The solution carefully considers the conditions for each valid subarray type and builds up the validity status incrementally based on the previous states. At the end of the iteration, the solution returns the validity status for the subarray with 3 consecutive increasing elements.

## Time Complexity

The time complexity of the solution is O(n), where n is the number of elements in the input array. The solution iterates through the array once, and each iteration involves constant-time operations.

## Space Complexity

The space complexity of the solution is O(1), as it only uses a constant amount of extra space to store the `dp` values and other variables.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!