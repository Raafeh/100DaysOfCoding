# Find the Duplicate Number

## Problem Description

You are given an array `nums` with integers, and there is a single integer in the array that appears more than once. Your goal is to find and return this repeated number. The array `nums` has the following characteristics:

- It contains `n + 1` integers where each integer is in the range `[1, n]`.
- There is only one repeated number in the array.

## Example

### Input:

```python
nums = [1, 3, 4, 2, 2]
```

### Output:

```python
2
```

### Input:

```python
nums = [3, 1, 3, 4, 2]
```

### Output:

```python
3
```

## Approach and Solution

We can solve this problem efficiently using Floyd's Tortoise and Hare (Cycle Detection) algorithm, which works as follows:

1. Initialize two pointers, `slow` and `fast`, both starting at the first element of the array.

2. Move the `slow` pointer one step at a time and the `fast` pointer two steps at a time until they meet in a cycle. This step is guaranteed to terminate because there is only one repeated number in the array.

3. After finding the meeting point, reset the `slow` pointer to the beginning of the array.

4. Move both pointers one step at a time until they meet again. The point where they meet is the entrance to the cycle and represents the repeated number.

This algorithm works without modifying the input array and uses only constant extra space.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input array `nums`. This is because both pointers traverse the array once.

### Space Complexity

The space complexity is O(1), as we are using a constant amount of extra space to store the `slow` and `fast` pointers.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
