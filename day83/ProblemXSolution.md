# Removing Duplicate Letters

## Problem Description

Given a string `s`, the goal is to remove duplicate letters so that every letter appears once and only once in the result string. The output string must be the smallest possible lexicographical order among all possible results.

**Example 1:**
```
Input: s = "bcabc"
Output: "abc"
```

**Example 2:**
```
Input: s = "cbacdcbc"
Output: "acdb"
```

## Approach and Solution

The solution to this problem involves a stack-based approach to maintain the desired order of characters while removing duplicates. Here's a detailed explanation of the solution:

1. Create a dictionary `last_occurrence` to keep track of the last occurrence of each character in the input string `s`.
2. Initialize an empty stack `stack` to build the result string.
3. Create an empty set `seen` to keep track of characters that are already in the stack.
4. Iterate through the characters of the input string `s`.
5. For each character `char`, check if it's not in the `seen` set. If it's not, proceed to the next steps.
6. Use a `while` loop to check if it's beneficial to pop characters from the `stack`:
   - Pop characters from the `stack` if the character at the top of the stack is greater than the current character `char`.
   - Ensure that there is a remaining occurrence of the character in the string (checked using `last_occurrence`) after the current index `i`.
7. After the loop, add the current character `char` to the `stack` and mark it as seen in the `seen` set.
8. Finally, join the characters in the `stack` to form the result string, which will be the smallest lexicographical order without duplicate letters.


- Time Complexity: The algorithm iterates through the input string `s` once and performs stack operations. Since each character is processed only once, the time complexity is O(n), where n is the length of the input string.

- Space Complexity: The algorithm uses additional data structures like the `last_occurrence` dictionary, `stack`, and `seen` set. In the worst case, where all characters in `s` are distinct, the space complexity is O(n) to store these data structures.