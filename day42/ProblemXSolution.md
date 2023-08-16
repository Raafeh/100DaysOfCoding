# Common Characters 

## Problem Description

Given an array of strings `words`, the goal is to return an array containing all characters that appear in every string within the `words` array, while considering duplicates. The order of characters in the output array does not matter.

**Example 1:**
```
Input: words = ["bella", "label", "roller"]
Output: ["e", "l", "l"]
```

**Example 2:**
```
Input: words = ["cool", "lock", "cook"]
Output: ["c", "o"]
```

## Approach and Solution

The solution leverages Python's `Counter` class, which is part of the `collections` module, to efficiently count the occurrences of characters in each string. The basic approach involves these steps:

1. Create a `Counter` for the characters in the first word.
2. Iterate through the remaining words and update the common characters' `Counter` by performing element-wise intersection with each word's `Counter`.
3. Convert the common characters' `Counter` into a list of characters, accounting for their frequencies.


**Time Complexity:** 
The solution iterates through each character in all the words, and for each character, it performs an intersection operation using the `&=` operator. The `Counter` operations and the iteration contribute to a time complexity of O(n * k), where n is the number of words and k is the average length of the words.

**Space Complexity:** 
The solution utilizes additional space to store `Counter` objects for the characters. The space complexity is O(m), where m is the number of unique characters in all words combined.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!