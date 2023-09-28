# Sort Array By Parity

## Problem Description

Given an array of integers, we want to sort the elements in such a way that all even numbers come first, followed by all odd numbers. 

### Example

Input: `[3, 1, 2, 4]`

Output: `[2, 4, 3, 1]`

## Approach and Solution

We can solve this problem by iterating through the input array and dividing the elements into two separate lists: one for even numbers and another for odd numbers. After separating the elements, we can concatenate the two lists to get the desired result.

Here's the step-by-step solution:

1. Initialize two empty lists, `stack` and `odds`, to store even and odd numbers, respectively.
2. Iterate through the input array `nums`. For each element `n` in `nums`, do the following:
   - If `n` is even (i.e., `n % 2 == 0`), add it to the `stack` list.
   - If `n` is odd, add it to the `odds` list.
3. After iterating through `nums`, extend the `stack` list by adding all elements from the `odds` list. This operation places all even elements at the beginning, followed by odd elements.
4. Return the `stack` list as the sorted array.

### Time Complexity

The time complexity of this solution is O(N), where N is the number of elements in the input array `nums`. We iterate through `nums` once to separate even and odd elements, and extending the `stack` list with elements from the `odds` list also takes O(N) time.

### Space Complexity

The space complexity of this solution is O(N), as we create two additional lists, `stack` and `odds`, to store the even and odd elements from `nums`. The space required for these lists is proportional to the size of the input array. However, the space complexity is still linear with respect to the input size.