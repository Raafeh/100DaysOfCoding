# Subsequence Checker

## Problem Statement

Given two strings, `s` and `t`, the task is to determine whether `s` is a subsequence of `t`.

**Example 1:**
- Input: `s = "abc"`, `t = "ahbgdc"`
- Output: `True`
- Explanation: "abc" is a subsequence of "ahbgdc" because we can obtain "abc" by deleting some characters from "ahbgdc" (e.g., removing "h", "b", and "g").

**Example 2:**
- Input: `s = "axc"`, `t = "ahbgdc"`
- Output: `False`
- Explanation: "axc" is not a subsequence of "ahbgdc" because "x" from `s` cannot be found in the same order in `t`.

## Solution

We can solve this problem efficiently by iterating through both strings, `s` and `t`, and checking if the characters in `s` are present in `t` in the same order. Here's a step-by-step explanation of the solution:

1. Initialize two pointers, `i` and `j`, to 0. These pointers will help us traverse `s` and `t`, respectively.
2. Use a while loop to iterate through both strings, `s` and `t`.
3. Inside the loop, check if the character at the current position of `s[i]` matches the character at the current position of `t[j]`.
4. If there is a match, increment the `i` pointer to move to the next character in `s`. This indicates that we have found a character from `s` in the same order in `t`.
5. Regardless of whether there is a match or not, always increment the `j` pointer to move to the next character in `t`.
6. Finally, after exiting the loop, check if the `i` pointer has reached the end of `s`. If it has, it means all characters in `s` have been found in `t` in the same order, and we return `True`. Otherwise, we return `False`.


**Time Complexity:** The time complexity of this solution is O(len(s) + len(t)), where len(s) and len(t) are the lengths of the input strings `s` and `t`. This is because we traverse both strings once, and the loop terminates when we reach the end of either string.

**Space Complexity:** The space complexity of this solution is O(1) because we use a constant amount of extra space to store the two pointers `i` and `j`. The solution does not use any additional data structures that depend on the input size.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
