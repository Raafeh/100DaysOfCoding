# Most Common Word 


## Problem Description

Given a paragraph and a list of banned words, the goal is to find the most frequent word in the paragraph that is not in the banned list. The paragraph may contain various punctuation marks and is case-insensitive. The output should be in lowercase.

### Example

**Input:**
```python
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
```

**Output:**
```python
"ball"
```

In this example, the word "hit" is banned, so it's excluded from consideration. The word "ball" occurs twice, more than any other non-banned word, making it the most frequent.

## Approach and Solution

The solution approach can be broken down into the following steps:

1. Preprocess the paragraph: Remove punctuation and convert to lowercase.
2. Split the paragraph into individual words.
3. Create a dictionary to store the frequency of each word.
4. Iterate through the words and update the frequency dictionary, excluding banned words.
5. Iterate through the frequency dictionary to find the most frequent non-banned word.



- Time Complexity: O(n), where n is the length of the paragraph. The preprocessing and word counting operations are linear with respect to the paragraph length.

- Space Complexity: O(m), where m is the number of unique non-banned words in the paragraph. The space is used to store the frequency counts of words in the dictionary.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!