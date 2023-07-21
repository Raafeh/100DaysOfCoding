# Number of Longest Increasing Subsequence

## Problem Description

Given an integer array `nums`, you need to find the number of longest increasing subsequences. A sequence is considered increasing if each element is strictly greater than the previous element.

### Example 1:
Input: nums = [1, 3, 5, 4, 7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

### Example 2:
Input: nums = [2, 2, 2, 2, 2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so the output is 5.

## Approach and Solution

To solve this problem efficiently, we will use dynamic programming. We'll maintain two arrays `dp_lengths` and `dp_counts` of the same length as the input `nums`. The `dp_lengths` array will keep track of the length of the longest increasing subsequence ending at each index, and the `dp_counts` array will keep track of the count of such subsequences ending at each index.

We start with both `dp_lengths` and `dp_counts` initialized to 1, as each element in `nums` can be a valid subsequence of length 1.

We then traverse the input array `nums` from left to right. For each element at index `i`, we look at all elements before it (from index 0 to `i-1`). If we find an element at index `j` such that `nums[i] > nums[j]`, it means we can extend the increasing subsequence ending at `j` with the current element at `i`.

We update the `dp_lengths` array by taking the maximum value between the current length at index `i` and the length at index `j + 1`. Additionally, we update the `dp_counts` array in the following way:

1. If the length at index `j + 1` is greater than the length at index `i`, we set the count at index `i` to be the same as the count at index `j`.
2. If the length at index `j + 1` is equal to the length at index `i`, we increment the count at index `i` by the count at index `j`.

After the traversal, we find the maximum length from the `dp_lengths` array, which gives us the length of the longest increasing subsequence.

Finally, we loop through both `dp_lengths` and `dp_counts` arrays. If the length at an index matches the maximum length, we add the corresponding count to the answer since those subsequences will be the longest increasing subsequences.

The time complexity of the solution is O(n^2), where n is the number of elements in the input array `nums`. This is because, in the worst case, we perform a nested loop over all elements to compare and update the `dp_lengths` and `dp_counts` arrays.

The space complexity of the solution is O(n), where n is the number of elements in the input array `nums`. We use two additional arrays `dp_lengths` and `dp_counts`, each of the same length as the input array, to store the intermediate results. Hence, the space complexity is linear with respect to the size of the input array.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!