# Minimum Deletions to Make Character Frequencies Unique

## Problem Description

A string is considered "good" if no two different characters in the string have the same frequency. In other words, a string is good if all its characters have unique frequencies. The goal is to find the minimum number of character deletions required to make a given string good.

### Example

**Input:** `"aaabbbcc"`

**Output:** `2`

**Explanation:** You can delete two 'b's resulting in the good string "aaabcc". Another way is to delete one 'b' and one 'c', resulting in the good string "aaabbc".

## Solution

The solution to this problem involves the following steps:

1. Initialize a dictionary to count the frequency of each character in the string.
2. Iterate through the string and count the frequency of each character, updating the dictionary.
3. Initialize a set to keep track of unique frequencies.
4. Iterate through the values in the frequency dictionary and add each frequency to the set. If a frequency is already in the set, increment it until it's unique.
5. Calculate the total number of deletions needed by summing up all the frequencies in the dictionary that are not in the set of unique frequencies.
6. Return the total number of deletions as the result.


- **Time Complexity:** The code iterates through the input string once to count the frequencies and then iterates through the frequency dictionary. Therefore, the time complexity is O(N), where N is the length of the input string.

- **Space Complexity:** The code uses additional space to store the frequency dictionary and the set of unique frequencies. In the worst case, where all characters have the same frequency, the space complexity is O(N), where N is the number of unique characters in the string.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
