# Minimum Replacements to Sort the Array 

## Problem Description

Given a 0-indexed integer array `nums`, the goal is to sort it in non-decreasing order using the minimum number of operations. In each operation, an element can be replaced with two elements that sum up to the original element.

**Example 1:**
```
Input: nums = [3, 9, 3]
Output: 2
Explanation:
- Replace the 9 with 3 and 6: [3, 3, 6, 3]
- Replace the 6 with 3 and 3: [3, 3, 3, 3, 3]
Total operations: 2
```

**Example 2:**
```
Input: nums = [1, 2, 3, 4, 5]
Output: 0
Explanation: The array is already in non-decreasing order, so no operations are needed.
```

## Approach and Solution 

The given problem can be efficiently solved using a greedy approach. The idea is to traverse the array in reverse order and iteratively calculate the operations needed for each element.

1. Initialize the variable `last` with the value of the last element of the array.
2. Initialize the variable `ans` to keep track of the total operations needed.
3. Traverse the array in reverse order, starting from the second-to-last element.
4. For each element at index `i`, compare it with `last`:
   - If `nums[i]` is greater than `last`, calculate how many times it needs to be divided to reach `last`. Add this value (`t - 1`) to `ans`.
   - Update `last` to be the result of the division.
   - If `nums[i]` is not greater than `last`, update `last` with the value of `nums[i]`.
5. After the traversal is complete, return the value of `ans` as the minimum number of operations required.

### Time Complexity

The time complexity of the solution is O(N), where N is the number of elements in the input array. The algorithm iterates through the array once in reverse order, performing constant-time operations for each element.

### Space Complexity

The space complexity of the solution is O(1), as it only uses a constant amount of extra space to store variables (`last` and `ans`) regardless of the input size.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!