# Integer Break 

## Problem Description

Given an integer `n`, you need to break it into the sum of `k` positive integers, where `k` is greater than or equal to 2, in such a way that you maximize the product of those integers. Return the maximum product you can achieve.

### Example 1
**Input:** `n = 2`
**Output:** `1`
**Explanation:** `2` can only be broken into `1 + 1`, and the product is `1 * 1 = 1`.

### Example 2
**Input:** `n = 10`
**Output:** `36`
**Explanation:** `10` can be broken into `3 + 3 + 4`, and the product is `3 * 3 * 4 = 36`.

## Approach and Solution

We can solve this problem using dynamic programming. Here's a step-by-step explanation of the solution:

1. Initialize a list `dp` of size `n + 1` to store the maximum product for each number from `2` to `n`.
2. Set the base case `dp[2] = 1` since `2` can only be broken into `1 + 1`.
3. Iterate over numbers from `3` to `n` and for each number `i`:

   a. Initialize a loop to try breaking `i` into two parts: `j` and `i - j`.
   b. For each `j` from `1` to `i // 2`, calculate the product of the maximum of `j` and `dp[j]` with the maximum of `i - j` and `dp[i - j]`. Update `dp[i]` with the maximum value.
4. The final result is stored in `dp[n]`, which represents the maximum product of breaking the integer `n` into `k` positive integers.

### Time Complexity

The time complexity of this solution is O(n^2) because we have a nested loop where the outer loop iterates from `3` to `n`, and the inner loop can go up to `n // 2` in the worst case.

### Space Complexity

The space complexity is O(n) as we need to store the `dp` array of size `n + 1` to store the maximum products for each number from `2` to `n`.
