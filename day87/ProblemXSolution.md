# 132 Pattern

## Problem Description

Given an array of `n` integers `nums`, a "132 pattern" is a subsequence of three integers `nums[i]`, `nums[j]`, and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

The task is to determine whether a "132 pattern" exists in the given array `nums`. If it exists, return `true`, otherwise return `false`.

### Example

**Input:**
```python
nums = [3, 1, 4, 2]
```

**Output:**
```python
True
```

**Explanation:**
In the input array, the 132 pattern is `[1, 4, 2]`, where `1` is `nums[i]`, `4` is `nums[j]`, and `2` is `nums[k]`. Thus, the function should return `True`.

## Approach and Solution 

The solution to this problem involves using a stack and iterating through the input array to identify a "132 pattern." Here's a high-level overview of the solution:

1. Initialize an array `min_left` to store the minimum value to the left of each element in `nums`. This helps us keep track of the minimum value as we traverse the array.
2. Create an empty stack to hold potential elements for the "132 pattern."
3. Iterate through the `nums` array from right to left.
4. For each element `nums[j]`, compare it with the corresponding `min_left[j]`. If `nums[j]` is greater than `min_left[j]`, it means there's a possibility of a "132 pattern."
5. While the stack is not empty and contains elements less than or equal to `min_left[j]`, pop those elements from the stack. This ensures that the stack only contains potential candidates for the "132 pattern."
6. If the stack is not empty and the top element of the stack is less than `nums[j]`, we have found a "132 pattern," and we return `True`.
7. Finally, if no "132 pattern" is found after iterating through the entire array, return `False`.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we iterate through the array once from right to left and perform constant-time operations for each element.

### Space Complexity

The space complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we use additional arrays (`min_left`) and a stack to store intermediate values, and the maximum space required is proportional to the length of the input array.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
