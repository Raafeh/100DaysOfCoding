# Longest Common Prefix 


## Problem Description

Given an array of strings, we need to find the longest common prefix among all the strings. If there is no common prefix, the function should return an empty string.

### Examples

**Example 1:**
```
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

**Example 2:**
```
Input: strs = ["dog", "racecar", "car"]
Output: ""
```

## Approach and Solution


The solution works as follows:

1. We first check if the input list `strs` is empty. If it is, we return an empty string since there's no common prefix to find.

2. We find the shortest string in the `strs` list using the `min` function and the `key=len` argument. This is because the common prefix cannot be longer than the shortest string.

3. We then iterate over the characters of the shortest string.

4. For each character, we compare it with the corresponding character in all other strings. If we find a character that doesn't match in any of the strings, we return the common prefix found so far (up to the current character).

5. If all characters match across all strings, we return the entire shortest string as the common prefix.

## Time Complexity

The time complexity of this solution is determined by the length of the shortest string in the input list, denoted as `n`. In the worst case, we may need to iterate through all `n` characters of the shortest string and compare them with all strings in the list. Since there are `m` strings in the list (where `m` is the length of the input list), the overall time complexity is O(n * m).

## Space Complexity

The space complexity of the solution is O(1) since the amount of additional space used by the algorithm does not increase with the input size. We only use a constant amount of space to store variables such as the shortest string and loop counters.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!