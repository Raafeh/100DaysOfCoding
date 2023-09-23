# Longest String Chain

## Problem Description

Given an array of words, each consisting of lowercase English letters, we want to find the length of the longest possible word chain. A word chain is a sequence of words, where each word is a predecessor of the next word. A word 'wordA' is considered a predecessor of 'wordB' if we can insert exactly one letter anywhere in 'wordA' without changing the order of the other characters to make it equal to 'wordB'.


## Example

### Input:

```python
words = ["a","b","ba","bca","bda","bdca"]
```

### Output:

```
4
```

Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

## Solution

We can solve this problem using dynamic programming. Here's a step-by-step explanation of the solution:
1. Sort the input words by length in ascending order. This step ensures that we process shorter words before longer ones since longer words are less likely to be predecessors of shorter words.
2. Initialize a dictionary `max_chain_length` to store the maximum chain length for each word.
3. Initialize a variable `result` to 1. This variable will store the length of the longest word chain found.
4. Iterate through the sorted words:
   - For each word, initialize the chain length for that word as 1 since any word can form a chain of length 1 by itself.
5. For each word, generate all possible predecessor words by removing one character at a time. Check if each predecessor exists in the `max_chain_length` dictionary and has a longer chain length. If so, update the chain length for the current word.
6. During this process, keep track of the maximum chain length overall by updating the `result` variable whenever a longer chain is found.
7. Finally, return the value of `result` as the length of the longest possible word chain.

### Time Complexity

- Time Complexity: The time complexity of this solution is O(N * M^2), where N is the number of words in the input list, and M is the maximum length of a word. The primary loop iterates through each word, and for each word, we generate possible predecessors, which takes O(M^2) time in the worst case.

### Space Complexity

- Space Complexity: The space complexity is O(N) because we store the maximum chain length for each word in the `max_chain_length` dictionary, where N is the number of words in the input list.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
