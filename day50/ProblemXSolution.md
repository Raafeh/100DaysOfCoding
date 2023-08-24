# Text Justification

## Problem Description

Given an array of strings `words` and a width `maxWidth`, the goal is to format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified. Extra spaces between words should be distributed as evenly as possible, with the empty slots on the left assigned more spaces than the slots on the right. For the last line of text, it should be left-justified, and no extra space is inserted between words.

### Example

**Input:**
```python
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

**Output:**
```
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

## Approach and Solution 

The given problem can be solved using a greedy approach. We iterate through the list of words, trying to pack as many words as possible into each line while respecting the `maxWidth` constraint. We also calculate how many extra spaces need to be added between words to achieve the desired line width.

1. We maintain a list called `line` to keep track of the words in the current line and a variable `line_length` to keep track of the total length of words in the line.

2. For each word in the `words` list:
   - If adding the word to the current line does not exceed `maxWidth`, we add it to the line and update `line_length`.
   - If adding the word would exceed `maxWidth`, we format the current line using the `format_line` function (explained below), add it to the result, and start a new line with the current word.

3. After processing all the words, we have the last line left. We left-justify the words in the last line and add it to the result.

4. The `format_line` function is used to evenly distribute the extra spaces between words in a line. If there's only one word in the line, we simply left-justify it. Otherwise, we calculate the total spaces needed, divide it by the number of gaps between words, and add any remaining spaces to the left gaps.

### Time and Space Complexity

The time complexity of the solution is O(N), where N is the total number of characters in the input list of words. This is because we iterate through each word once.

The space complexity is O(M), where M is the number of words in the input list. This is because we use the `line` list to store the words in the current line, which can have at most M words.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!