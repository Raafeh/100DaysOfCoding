# Reverse Words in a Sentence

## Problem Description

Given a string `s`, you are tasked with reversing the order of characters in each word within a sentence while still preserving whitespace and initial word order.

### Examples:

- Input: "Let's take LeetCode contest"
  Output: "s'teL ekat edoCteeL tsetnoc"

- Input: "God Ding"
  Output: "doG gniD"

## Approach and Solution

We can solve this problem by following these steps:

1. Split the input string `s` into individual words. We can do this by using whitespace as a delimiter, which will give us a list of words.
2. Iterate through the list of words. For each word, reverse its characters using slicing and update the word in the list.
3. Finally, join the reversed words back together using whitespace as a separator to form the reversed sentence.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`. This is because we split the string into words, iterate through each word to reverse it, and then join the words back together, all of which are linear operations.

### Space Complexity

The space complexity is also O(n) because we create lists to store the words and reversed words, which can grow linearly with the input string size.
