# Decoding String at Index

## Problem Statement

You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time, and the following steps are taken:

1. If the character read is a letter, that letter is written onto the tape.
2. If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.

Given an integer `k`, you need to return the kth letter (1-indexed) in the decoded string.

### Example

**Input:**
```python
s = "leet2code3"
k = 10
```

**Output:**
```
"o"
```

**Explanation:**
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

## Approach and Solution

To solve this problem efficiently, we can simulate the decoding process step by step without actually decoding the entire string. Here's a high-level overview of the solution:

1. Initialize a variable `size` to keep track of the size of the decoded string.
2. Iterate through the characters in the input string `s`. If a character is a digit, we multiply the `size` by that digit minus 1; otherwise, we increment `size` by 1.
3. Traverse the string in reverse order, starting from the last character.
4. For each character, calculate `k % size` to determine its relative position in the current block. If `k % size` becomes zero, and the character is alphabetic, return that character as the result.
5. Update `size` accordingly. If the character is a digit, divide `size` by that digit; otherwise, decrement `size` by 1.

This approach allows us to find the kth letter efficiently without decoding the entire string.

### Time Complexity

The time complexity of this solution is O(N), where N is the length of the input string `s`. This is because we iterate through the string twice, once to calculate the size and once to find the kth letter.

### Space Complexity

The space complexity is O(1) since we use a constant amount of extra space regardless of the input size.