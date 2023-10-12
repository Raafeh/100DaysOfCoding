# Valid Anagram 

## Problem Statement

Given two strings `s` and `t`, the task is to determine whether `t` is an anagram of `s`.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. This repository provides a Python solution to determine whether two given strings are anagrams of each other.

**Examples:**

- Input: `s = "anagram"`, `t = "nagaram"`
  Output: `true`

- Input: `s = "rat"`, `t = "car"`
  Output: `false`

## Approach and Solution

The provided Python solution uses a straightforward approach to check if two strings are anagrams. Here's a breakdown of the solution:

1. First, the solution checks if the lengths of the two input strings `s` and `t` are equal. If their lengths are different, it immediately returns `false` since two strings with different lengths cannot be anagrams.
2. The solution then creates a dictionary called `char_count` to count the occurrences of each character in string `s`.
3. It iterates through string `s`, updating the counts in the `char_count` dictionary.
4. Next, it iterates through string `t` and attempts to decrement the counts of the characters in the `char_count` dictionary to simulate the cancellation of characters. If a character in `t` is not found in the dictionary, it returns `false` because it indicates that `t` contains a character that is not present in `s`.
5. If the iteration through `t` completes without returning `false`, it checks whether the `char_count` dictionary is empty. If the dictionary is empty, it means that all characters in `s` and `t` canceled out, and they are indeed anagrams.
6. The function returns `true` if the dictionary is empty or `false` otherwise.

- **Time Complexity:** The solution iterates through both strings `s` and `t` once, so the time complexity is O(n), where n is the length of the input strings.

- **Space Complexity:** The solution uses a dictionary `char_count` to store character counts for string `s`. In the worst case, it can store all unique characters from `s`. Therefore, the space complexity is O(c), where c is the number of unique characters in `s`.
