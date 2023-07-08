# Maximize the Confusion of an Exam

## Problem Description

You are a teacher preparing a test with `n` true/false questions. To make things more challenging, you want to maximize the number of consecutive questions with the same answer, either true or false. This will surely confuse the students!

You are given a string `answerKey`, where `answerKey[i]` represents the original answer to the `ith` question. Additionally, you have an integer `k`, which represents the maximum number of times you can perform the following operation:

- Change the answer key for any question to 'T' (true) or 'F' (false).

Your task is to determine the maximum number of consecutive 'T's or 'F's in the answer key, considering that you can perform at most `k` operations.

## Example
```
Input: answerKey = "TTFF", k = 2
Output: 4
```
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's

## Approach and Solution

To solve this problem, we can use a sliding window approach. Here's a step-by-step explanation of the algorithm:

1. Initialize variables `tCount` and `fCount` to keep track of the count of 'T's and 'F's, respectively.
2. Set `maxCount` to 0 to store the maximum number of consecutive 'T's or 'F's.
3. Initialize two pointers, `left` and `right`, to track the window boundaries. Set them both to 0 initially.
4. Iterate through the answer key from left to right:
    - If the current element is 'T', increment `tCount` by 1; otherwise, increment `fCount` by 1.
    - Check if the maximum count of either 'T's or 'F's within the window (i.e., `tCount` or `fCount`) plus the number of remaining operations (`k`) is greater than or equal to the current window size (`right - left + 1`).
        - If it is, update `maxCount` if necessary by comparing it with the current window size.
        - If not, move the left pointer to the right, updating `tCount` and `fCount` accordingly, to maintain the window size.
    - Move the right pointer to the right.
5. Return the `maxCount` obtained during the process, which represents the maximum number of consecutive 'T's or 'F's that can be achieved after performing at most `k` operations.

The time complexity of this solution is O(n), where n is the length of the answer key, as we iterate through the key only once. The space complexity is O(1), as we use a fixed amount of extra space to store variables and pointers.

