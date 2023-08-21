# Repeated Substring Pattern


## Problem Description

Given a string `s`, the goal is to check if it can be formed by repeating a substring of itself. In other words, we need to determine if there exists a substring that, when repeated multiple times, forms the original string `s`.

**Example 1:**
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" repeated twice.

**Example 2:**
Input: s = "aba"
Output: false

**Example 3:**
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" repeated four times or the substring "abcabc" repeated twice.

## Approach and Solution

The provided Python solution uses a straightforward approach to solve this problem. The main idea is to iterate through possible substring lengths and check if the given string `s` can be formed by repeating a substring of length `i` for various values of `i`.

1. Calculate the length of the input string `s` and store it as `n`.
2. Iterate over possible substring lengths `i` from 1 to `n//2` (inclusive).
3. For each `i`, check if `n` is divisible by `i`. If not, move on to the next `i`.
4. If `n` is divisible by `i`, construct a pattern by repeating the substring `s[:i]` `(n//i)` times.
5. Compare the constructed pattern with the original string `s`. If they match, return `True` as the original string can be formed by repeating the substring.
6. If no valid substring length is found that forms the given string, return `False`.


- **Time Complexity:** The provided solution has a time complexity of O(n^2) due to the loop that iterates over possible substring lengths and the substring repetition inside the loop.
- **Space Complexity:** The space complexity is O(n), where `n` is the length of the input string `s`. This is primarily due to the space required to store the pattern string constructed for comparison.

