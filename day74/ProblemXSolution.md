# Buddy Strings

## Problem Description

Given two strings `s` and `goal`, return `true` if you can swap two letters in `s` so the result is equal to `goal`, otherwise, return `false`.

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

## Examples

- Input: `s = "ab", goal = "ba"`
  Output: `true`
  Explanation: You can swap `s[0] = 'a'` and `s[1] = 'b'` to get "ba", which is equal to `goal`.

- Input: `s = "ab", goal = "ab"`
  Output: `false`
  Explanation: The only letters you can swap are `s[0] = 'a'` and `s[1] = 'b'`, which results in "ba" != `goal`.

- Input: `s = "aa", goal = "aa"`
  Output: `true`
  Explanation: You can swap `s[0] = 'a'` and `s[1] = 'a'` to get "aa", which is equal to `goal`.

## Approach and Solution

The `buddyStrings` function checks if it's possible to make a single swap to transform `s` into `goal`. Here are the steps of the solution:

1. Check if the lengths of `s` and `goal` are not equal. If they are not equal, return `False` because you cannot make a valid swap.
2. Check if `s` is equal to `goal`. If they are equal, you need to check if there are duplicate characters in `s`. If there are duplicate characters, you can swap two identical characters to get the same string. So, return `True` if there are duplicates; otherwise, return `False`.
3. If `s` is not equal to `goal`, create two lists, `diff` and `swap`. Traverse through both `s` and `goal`, and if the characters at corresponding positions are not equal, append their indices to `diff`. At the same time, append the characters themselves to `swap`.
4. If the length of `diff` is not equal to 2, it means you can't make exactly one swap to make `s` equal to `goal`, so return `False`.
5. If the characters at the positions specified by the indices in `diff` are the same when swapped, return `True`; otherwise, return `False`.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input strings `s` and `goal`. This is because we iterate through both strings once.

### Space Complexity

The space complexity of this solution is O(n) because we use additional space to store the `diff` and `swap` lists, both of which can have a maximum length of 2n in the worst case.
