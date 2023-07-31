# Minimum ASCII Delete Sum for Two Strings

## Problem Description

Given two strings `s1` and `s2`, you need to find the lowest ASCII sum of deleted characters to make the two strings equal. In other words, you have to delete some characters from both strings such that the remaining characters are identical, and the sum of the ASCII values of the deleted characters is minimized.

For example:
- Input: `s1 = "sea"`, `s2 = "eat"`
  Output: `231`
  Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum. Deleting "t" from "eat" adds 116 to the sum. At the end, both strings are equal, and `115 + 116 = 231` is the minimum sum possible to achieve this.

- Input: `s1 = "delete"`, `s2 = "leet"`
  Output: `403`
  Explanation: Deleting "dee" from "delete" to turn the string into "let", adds `100[d] + 101[e] + 101[e]` to the sum. Deleting "e" from "leet" adds 101[e] to the sum. At the end, both strings are equal to "let", and the answer is `100 + 101 + 101 + 101 = 403`. If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

## Solution

To solve this problem, we can use dynamic programming. We create a 2D DP (Dynamic Programming) table to store the minimum ASCII sum of deleted characters. The DP table will have dimensions `(m + 1) x (n + 1)`, where `m` and `n` are the lengths of `s1` and `s2` respectively.

The idea is to fill the DP table iteratively by comparing characters between the two strings and calculating the minimum sum required to make them equal. We follow these steps:

1. Initialize the DP table and fill the first row and column with cumulative ASCII values of characters in `s1` and `s2` respectively. This is done to handle the cases where we need to delete all characters in one of the strings to make them equal to an empty string.

2. Traverse through the DP table from `(1, 1)` to `(m, n)` (inclusive) and apply the following rules:
   - If the characters at the current positions in both strings match, then no characters need to be deleted, so we copy the value from the diagonal (previous state without the characters) to the current cell.
   - If the characters don't match, we need to delete one of the characters. We calculate the minimum sum by choosing the minimum of the following two options:
     a) Delete the character from `s1` and add its ASCII value to the current cell value.
     b) Delete the character from `s2` and add its ASCII value to the current cell value.

3. The value in the bottom-right corner of the DP table will be the minimum ASCII sum of deleted characters required to make the two strings equal.

The final value in the bottom-right corner of the DP table will be our answer.

## Time and Space Complexity

The time complexity of the solution is O(m * n), where `m` and `n` are the lengths of `s1` and `s2` respectively. This is because we need to fill the entire DP table of dimensions `(m + 1) x (n + 1)`.

The space complexity of the solution is also O(m * n) since we use a 2D DP table to store the intermediate results. However, it is possible to optimize the space complexity to O(min(m, n)) by using two 1D arrays of size `min(m, n) + 1` instead of the 2D DP table, as we only need to keep track of the previous row/column while filling the DP table.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!