# Monotonic Array Checker

## Problem Description

Given an integer array `nums`, we need to determine if it is a monotonic array.

An array `nums` is considered monotonic increasing if, for all `i` <= `j`, `nums[i] <= nums[j]`. Similarly, `nums` is considered monotonic decreasing if, for all `i` <= `j`, `nums[i] >= nums[j]`.

## Approach and Solution

We can solve this problem by iterating through the array and checking if it is either strictly increasing or strictly decreasing. Here's how the solution works:

1. Initialize two boolean variables, `increasing` and `decreasing`, to `True`. These variables will keep track of whether the array is monotonic increasing or decreasing.
2. Iterate through the elements of the `nums` array starting from the second element (index 1) and compare each element with the previous one.
3. If we encounter a pair of elements where `nums[i]` is greater than `nums[i-1]`, we set the `decreasing` variable to `False` because the array is not decreasing in this case.
4. If we encounter a pair of elements where `nums[i]` is less than `nums[i-1]`, we set the `increasing` variable to `False` because the array is not increasing in this case.
5. After iterating through the entire array, if neither `increasing` nor `decreasing` is `False`, it means the array is either strictly increasing or strictly decreasing, and we return `True`. Otherwise, we return `False`.

### Time Complexity

The time complexity of this solution is O(n), where n is the number of elements in the `nums` array. We iterate through the array once, comparing adjacent elements.

### Space Complexity

The space complexity of this solution is O(1), as we only use a constant amount of extra space to store the `increasing` and `decreasing` boolean variables. The space required does not depend on the size of the input array.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
