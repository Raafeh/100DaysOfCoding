# Reverse Vowels in a String

## Problem

Given a string `s`, the task is to reverse only the vowels in the string and return the modified string. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lowercase and uppercase.

### Example

**Input:**
```
s = "hello"
```
**Output:**
```
"holle"
```

**Input:**
```
s = "leetcode"
```
**Output:**
```
"leotcede"
```

## Approach and Solution

To solve this problem, we can use a two-pointer approach. We initialize two pointers, `left` and `right`, pointing to the start and end of the string respectively. We iterate through the string from both ends, checking if the characters at `left` and `right` are vowels.

If the character at `left` is not a vowel, we increment `left` by 1. Similarly, if the character at `right` is not a vowel, we decrement `right` by 1. If both characters at `left` and `right` are vowels, we swap them and increment `left` by 1 and decrement `right` by 1.

We continue this process until `left` becomes greater than or equal to `right`, indicating that we have traversed the entire string. Finally, we convert the modified list back to a string and return it as the result.

The time complexity of this solution is O(n), where n is the length of the input string `s`. We iterate through the string once from both ends, performing constant-time operations such as character comparisons and swapping. 
The space complexity is O(n) as well, since we convert the string to a list of characters to modify individual characters.

Feel free to explore the provided code implementation and modify it to suit your needs. Happy coding!
