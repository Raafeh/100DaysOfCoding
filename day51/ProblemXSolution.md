# Interleaving String Problem

## Problem Description

Given three strings `s1`, `s2`, and `s3`, the task is to determine whether `s3` can be formed by interleaving the strings `s1` and `s2`. Interleaving of two strings refers to creating a configuration where the characters of the two strings are divided into substrings and then combined in such a way that the original order is maintained. 

The conditions for interleaving are as follows:
- The strings `s1` and `s2` are divided into substrings `s1 = s1_1 + s1_2 + ... + s1_n` and `s2 = s2_1 + s2_2 + ... + s2_m`.
- The combined string should be either `s1_1 + s2_1 + s1_2 + s2_2 + ...` or `s2_1 + s1_1 + s2_2 + s1_2 + ...`.

## Example

**Input:**
```
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
```
**Output:** True
**Explanation:** One way to obtain `s3` is by splitting `s1` into "aa" and "bc", and `s2` into "dbbc" and "a". Interleaving the two splits: "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

## Approach and Solution 

The solution employs dynamic programming to solve the problem efficiently. It uses a two-dimensional DP array where `dp[i][j]` represents whether the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i+j` characters of `s3`.

The recurrence relation is as follows:
- `dp[i][j]` is `True` if either `s1[i-1]` matches `s3[i+j-1]` and `dp[i-1][j]` is `True`, or `s2[j-1]` matches `s3[i+j-1]` and `dp[i][j-1]` is `True`.

Finally, the algorithm returns `dp[m][n]`, where `m` is the length of `s1` and `n` is the length of `s2`. If `dp[m][n]` is `True`, it indicates that `s3` can be formed by interleaving `s1` and `s2`.

### Time and Space Complexity

The time complexity of the solution is O(m * n), where `m` is the length of string `s1` and `n` is the length of string `s2`. The dynamic programming array of size `(m + 1) x (n + 1)` is filled in a nested loop.

The space complexity is also O(m * n) due to the DP array used to store the intermediate results.
