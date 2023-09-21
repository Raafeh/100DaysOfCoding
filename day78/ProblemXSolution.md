# Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, you need to find the median of the two sorted arrays. The overall run-time complexity should be O(log(min(m, n))).

**Example 1:**

Input: `nums1 = [1,3], nums2 = [2]`
Output: `2.00000`
Explanation: Merged array = `[1,2,3]` and the median is `2`.

**Example 2:**

Input: `nums1 = [1,2], nums2 = [3,4]`
Output: `2.50000`
Explanation: Merged array = `[1,2,3,4]` and the median is `(2 + 3) / 2 = 2.5`.

## Approach and Solution

To solve this problem efficiently with a time complexity of O(log(min(m, n))), we can use a binary search approach. The idea is to partition the two arrays in such a way that the elements on the left side are smaller or equal to the elements on the right side. Then, we can calculate the median based on these partitions.

Here's a step-by-step breakdown of the solution:

1. Ensure that `nums1` is the smaller array between the two. If not, swap them to make sure `nums1` is the smaller one.
2. Initialize variables `imin`, `imax`, and `half_len` for binary search:
   - `imin`: Starting index for binary search (initialized to 0).
   - `imax`: Ending index for binary search (initialized to the length of `nums1`).
   - `half_len`: Half the length of the combined arrays, rounded up to handle both even and odd total lengths.
3. Perform a binary search loop while `imin` is less than or equal to `imax`:
   - Calculate the index `i` as the average of `imin` and `imax`.
   - Calculate the index `j` as `half_len - i`.
4. Inside the loop, check if `i` and `j` are in the correct positions to create a valid partition:
   - If `i` is less than `m` (length of `nums1`) and `nums2[j - 1]` is greater than `nums1[i]`, it means we need to increase `i` to the right.
   - If `i` is greater than 0 and `nums1[i - 1]` is greater than `nums2[j]`, it means we need to decrease `i` to the left.
   - If the above conditions are not met, we have found the correct partition, and we proceed to calculate the median.
5. Calculate the maximum element on the left side (`max_of_left`):
   - If `i` is 0, it means there are no elements in `nums1` on the left side, so `max_of_left` is `nums2[j - 1]`.
   - If `j` is 0, it means there are no elements in `nums2` on the left side, so `max_of_left` is `nums1[i - 1]`.
   - Otherwise, calculate the maximum of `nums1[i - 1]` and `nums2[j - 1]`.
6. Check if the total number of elements in the combined arrays is odd:
   - If it's odd, return `max_of_left` as the median.
7. Calculate the minimum element on the right side (`min_of_right`):
   - If `i` is equal to `m`, it means there are no elements in `nums1` on the right side, so `min_of_right` is `nums2[j]`.
   - If `j` is equal to `n`, it means there are no elements in `nums2` on the right side, so `min_of_right` is `nums1[i]`.
   - Otherwise, calculate the minimum of `nums1[i]` and `nums2[j]`.
8. Return the median as `(max_of_left + min_of_right) / 2.0`.

### Time Complexity

The time complexity of this solution is O(log(min(m, n))), as it uses a binary search approach to find the correct partition in both arrays.

### Space Complexity

The space complexity is O(1) because it only uses a constant amount of additional space to store variables for the binary search.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
