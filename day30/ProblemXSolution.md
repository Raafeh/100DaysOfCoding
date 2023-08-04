# Word Break Problem

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, the task is to determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation.

### Examples

Example 1:
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
```

Example 3:
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Solution

To solve this problem, we can use dynamic programming. The idea is to build a dynamic programming table to store intermediate results. The `dp` array of size `n+1` (where `n` is the length of the input string `s`) will be used to determine if the prefix of the string can be segmented into words from the dictionary.

1. Initialize an empty set `wordSet` to store all the words from `wordDict`. This allows for faster word lookup.
2. Create a `dp` array of size `n+1`, where `dp[i]` will be `True` if `s[:i]` can be segmented into words from the dictionary, and `dp[0]` is always set to `True` as an empty string is always present in the dictionary.
3. Iterate through the string `s` from index 1 to `n`, and for each index `i`, iterate through the string from index 0 to `i`. For each index `j`, check if `dp[j]` is `True` (which means that the prefix `s[:j]` can be segmented), and if the substring `s[j:i]` is present in the `wordSet`.
4. If both conditions are met, update `dp[i]` to `True` and break out of the inner loop.
5. The final result will be stored in `dp[n]`, which indicates whether the entire string `s` can be segmented using the words from the dictionary.

### Time Complexity

The time complexity of the solution is O(n^2), where n is the length of the input string `s`. This is because, for each index `i`, we iterate through the string from index 0 to `i`.

### Space Complexity

The space complexity of the solution is O(n), where n is the length of the input string `s`. This is because we use the `dp` array of size `n+1` and the `wordSet` to store the words from `wordDict`.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!