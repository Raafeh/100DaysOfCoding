Certainly! Here's a `README.md` file for your GitHub repository, describing the problem and its solution:

---

# Majority Element II

## Problem Description

Given an integer array `nums` of size `n`, you are tasked with finding all elements that appear more than ⌊ n/3 ⌋ times. This problem can be challenging due to its requirement to find elements that occur more than a certain fraction of the total array size.

### Example 1:
Input: `nums = [3,2,3]`
Output: `[3]`

### Example 2:
Input: `nums = [1]`
Output: `[1]`

### Example 3:
Input: `nums = [1,2]`
Output: `[1,2]`

## Solution

To solve this problem efficiently, we can use the Boyer-Moore Majority Vote algorithm, modified to find elements that appear more than ⌊ n/3 ⌋ times. Here's a high-level overview of the solution:

1. We maintain two candidate elements (`candidate1` and `candidate2`) and their respective counts (`count1` and `count2`).

2. We iterate through the `nums` array and update the candidates and their counts as follows:
   - If the current element is equal to `candidate1`, we increment `count1`.
   - If the current element is equal to `candidate2`, we increment `count2`.
   - If `count1` becomes zero, we update `candidate1` to the current element and set `count1` to 1.
   - If `count2` becomes zero, we update `candidate2` to the current element and set `count2` to 1.
   - If neither `count1` nor `count2` is zero, we decrement both `count1` and `count2`.

3. After the first pass, we need to recompute the counts of `candidate1` and `candidate2` by iterating through the array once more.

4. Finally, we check if either of the candidates (`candidate1` or `candidate2`) appears more than ⌊ n/3 ⌋ times and add them to the result list if they do.

This algorithm guarantees that we find all elements that appear more than ⌊ n/3 ⌋ times and does so in linear time complexity.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input `nums` array. We traverse the array twice, and each traversal is a linear pass.

### Space Complexity

The space complexity of this solution is O(1), as we use only a constant amount of extra space to store variables (`candidate1`, `candidate2`, `count1`, `count2`, and `result`). We do not use any additional data structures that depend on the input size.
