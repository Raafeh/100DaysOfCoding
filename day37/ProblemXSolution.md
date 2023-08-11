# Coin Change II


## Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. The task is to determine the number of combinations that can make up the given amount using the provided coins. If it's not possible to make up the amount using any combination of the coins, the solution should return 0.

Assumptions:
- You have an infinite number of each kind of coin.
- The answer is guaranteed to fit into a signed 32-bit integer.

## Examples

**Example 1:**
```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: There are four ways to make up the amount:
5 = 5
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1
```

**Example 2:**
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up using only coins of denomination 2.
```

**Example 3:**
```
Input: amount = 10, coins = [10]
Output: 1
Explanation: There's only one way to make up the amount 10 using a coin of denomination 10.
```

## Approach and Solution

The solution to the "Coin Change 2" problem is based on dynamic programming. We use an array `dp`, where `dp[i]` represents the number of combinations to make up the amount `i` using the provided coin denominations. We initialize `dp[0]` to 1, as there's one way to make up amount 0 (using no coins).

For each coin denomination, we iterate through the `dp` array and update the number of combinations. Specifically, `dp[i] += dp[i - coin]` means that we're adding the number of combinations for the current amount `i - coin` to the current amount `i`.

Finally, we return `dp[amount]`, which contains the number of combinations to make up the given amount using the provided coins.

## Time and Space Complexity

- Time Complexity: O(amount * n), where `amount` is the given target amount and `n` is the number of coin denominations.
- Space Complexity: O(amount), as we use an array `dp` of size `amount + 1` to store the number of combinations for each amount.

This dynamic programming solution efficiently solves the problem and can handle relatively large inputs due to its polynomial time complexity.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!