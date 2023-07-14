# Longest Arithmetic Subsequence

## Problem Statement

Given an array `arr` and a difference `difference`, we need to find the length of the longest subsequence in `arr` that forms an arithmetic sequence with a difference of `difference`. A subsequence is a sequence that can be derived from `arr` by deleting some or no elements without changing the order of the remaining elements.

### Example

Input:
```
arr = [1, 2, 3, 4]
difference = 1
```

Output:
```
4
```

Explanation:
The longest arithmetic subsequence is [1, 2, 3, 4] with a difference of 1.

## Approach and Solution

To solve this problem, we can use dynamic programming. We'll create a dictionary to store the length of the longest arithmetic subsequence ending at each element in the input array.

For each element in the array, we'll check if there is a previous element in the array that forms an arithmetic sequence with a difference of `difference` with the current element. If such a previous element exists, we'll update the length of the arithmetic subsequence ending at the current element to be one more than the length of the subsequence ending at the previous element. Otherwise, we'll set the length of the subsequence ending at the current element to be 1.

Finally, we'll iterate through the dictionary and return the maximum length among all arithmetic subsequences.

The time complexity of this solution is O(n), where n is the length of the input array `arr`. This is because we iterate through the array once to populate the dictionary.

The space complexity is also O(n) since we use a dictionary to store the lengths of the arithmetic subsequences.

Feel free to explore the provided code implementation and modify it to suit your needs. Happy coding!
