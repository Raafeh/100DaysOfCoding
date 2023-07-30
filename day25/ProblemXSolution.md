# Strange Printer

## Problem Description

You have encountered a strange printer that has two special properties:

1. The printer can only print a sequence of the same character each time.
2. At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `s`, your task is to determine the minimum number of turns this strange printer needs to print the entire string.

### Examples

**Example 1:**

Input: `s = "aaabbb"`

Output: `2`

Explanation: The optimal strategy is to first print "aaa" and then print "bbb".

**Example 2:**

Input: `s = "aba"`

Output: `2`

Explanation: The optimal strategy is to first print "aaa" and then print "b" starting from the second place of the string, which will cover the existing character 'a'.

## Solution

To solve this problem, we can use dynamic programming. We'll create a 2D DP array to store the minimum number of turns for substrings. The DP array will be of size `n x n`, where `n` is the length of the input string `s`.

The idea behind the dynamic programming approach is to find the minimum turns for substrings of `s` and then combine them to find the minimum turns for the entire string.

1. For the base case, any single character requires one turn, so `dp[i][i] = 1` for all `i`.

2. We'll iterate through the string `s` in reverse order to fill the DP array.

3. For each pair of indices `i` and `j`, representing a substring of `s`, we'll check two cases:

   a. If the characters at both ends of the substring are the same, we can reduce the problem size by 1 and set `dp[i][j] = dp[i][j - 1]`.

   b. If the characters at both ends are different, we need to find the minimum turns by trying every possible break point `k` within the substring. The minimum turns for the substring will be `min(dp[i][j], dp[i][k] + dp[k + 1][j])` for all `k`.

4. The answer will be stored in `dp[0][n - 1]`, representing the minimum turns needed to print the entire string.

## Time Complexity

The time complexity of the dynamic programming solution is O(n^3), where n is the length of the input string `s`. This is because we have three nested loops to fill the DP array.

## Space Complexity

The space complexity of the dynamic programming solution is O(n^2) as we are using a 2D DP array of size `n x n` to store the minimum turns for substrings.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!