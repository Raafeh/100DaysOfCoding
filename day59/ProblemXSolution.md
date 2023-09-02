# Extra Characters in a String

## Problem Statement

Given a string `s` and a dictionary of words, your task is to break the string `s` into one or more non-overlapping substrings, such that each substring is present in the dictionary. There may be some extra characters in `s` that are not part of any substring. Your goal is to find and return the minimum number of extra characters left over if you break up `s` optimally.

## Example

**Input:**

```
s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
```

**Output:**

```
1
```

**Explanation:**

We can break `s` into two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

**Input:**

```
s = "sayhelloworld"
dictionary = ["hello", "world"]
```

**Output:**

```
3
```

**Explanation:**

We can break `s` into two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

## Approach and Solution

We can solve this problem using dynamic programming. Here's a high-level overview of the solution:

1. Initialize an array `dp` of length `n + 1` (where `n` is the length of the input string `s`) and set all elements to positive infinity, except for `dp[0]` which is set to 0.
2. Iterate through the string `s` from left to right, and at each position `i`, check all possible dictionary words that could end at position `i`.
3. If a match is found, update `dp[i]` with the minimum of its current value and `dp[i - len(word)]`, where `len(word)` is the length of the matched word.
4. Update `dp[i]` with the minimum of its current value and `dp[i - 1] + 1`, representing the case where we don't use any word ending at position `i`.
5. Finally, return `dp[n]`, where `n` is the length of the input string `s`, which represents the minimum number of extra characters needed to break the string optimally.

### Time Complexity

The time complexity of this solution is O(n * m), where `n` is the length of the input string `s`, and `m` is the total number of words in the dictionary. In the worst case, we iterate through the entire string for each word in the dictionary.

### Space Complexity

The space complexity is O(n), as we use an additional array `dp` of length `n + 1` to store intermediate results.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!