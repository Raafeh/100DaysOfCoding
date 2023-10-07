# Uncrossed Lines

## Problem Description

Given two integer arrays `nums1` and `nums2`, we want to find the maximum number of uncrossed lines we can draw between the two arrays. A line connects two numbers `nums1[i]` and `nums2[j]` if:

1. `nums1[i] == nums2[j]`
2. The line we draw does not intersect any other connecting (non-horizontal) line.

The task is to return the maximum number of connecting lines we can draw in this way.

### Example

**Example 1:**

Input: `nums1 = [1, 4, 2]`, `nums2 = [1, 2, 4]`

Output: `2`

Explanation: We can draw 2 uncrossed lines as shown below:

```
   1 4 2
   | |
   1 2 4
```

We cannot draw 3 uncrossed lines because connecting `nums1[1] = 4` to `nums2[2] = 4` will intersect the line from `nums1[2] = 2` to `nums2[1] = 2`.

## Approach and Solution

We can solve this problem using dynamic programming. We'll create a 2D array `dp` to represent the maximum number of uncrossed lines at each pair of indices in `nums1` and `nums2`. The steps are as follows:

1. Initialize `dp` with dimensions `(m+1) x (n+1)`, where `m` and `n` are the lengths of `nums1` and `nums2`, respectively. This array will store the maximum number of uncrossed lines for subproblems.

2. Iterate through `nums1` and `nums2` using nested loops, comparing each pair of elements. If `nums1[i]` is equal to `nums2[j]`, then we can extend the maximum number of uncrossed lines by 1, so we update `dp[i+1][j+1] = dp[i][j] + 1`.

3. If the elements are not equal, we take the maximum of either extending the line from `nums1` (i.e., `dp[i][j+1]`) or extending the line from `nums2` (i.e., `dp[i+1][j]`).

4. Finally, `dp[m][n]` will contain the maximum number of uncrossed lines between `nums1` and `nums2`, and we return this value as the result.

### Time Complexity

The time complexity of this solution is O(m * n), where `m` and `n` are the lengths of `nums1` and `nums2`, respectively. This is because we iterate through both arrays once to fill in the `dp` array.

### Space Complexity

The space complexity of this solution is O(m * n) as well, as we use a 2D array `dp` of the same dimensions to store the maximum number of uncrossed lines for each subproblem.
