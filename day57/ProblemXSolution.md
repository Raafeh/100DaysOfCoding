# Minimum Taps to Water Garden 


## Problem Statement

You have a one-dimensional garden on the x-axis, starting at point 0 and ending at point n. There are n + 1 taps located at various points in the garden. Each tap has a range, represented by an integer value, which indicates the area it can water. The goal is to determine the minimum number of taps that need to be opened to water the entire garden. If it's not possible to water the entire garden, the function should return -1.

## Example

For instance, consider the following example:

```
Input: n = 5, ranges = [3, 4, 1, 1, 0, 0]
Output: 1
Explanation: The tap at point 1 can cover the interval [-3, 5]. Opening only the second tap will water the whole garden [0, 5].
```

## Approach and Solution 

The problem can be solved using a greedy algorithm. The main idea is to treat the taps as intervals and find the minimum number of intervals needed to cover the entire garden. Here's how the solution approach works:

1. Convert tap ranges into intervals: Convert each tap's range into an interval in the format (start, end), where `start` is the left boundary of the area the tap can water, and `end` is the right boundary.
2. Sort intervals: Sort the intervals based on their starting point. This step ensures that we process intervals in a consistent order.
3. Iterate through intervals: Iterate through the sorted intervals. Keep track of the current interval's `start` and `end`. Also, keep track of the farthest point reachable using the taps opened so far.
4. Update farthest point: Whenever an interval's starting point is greater than the current farthest point, it means a gap exists that cannot be covered. In this case, return -1, as it's not possible to water the entire garden.
5. Use taps optimally: Whenever the current interval's starting point is greater than the current end, it means we need to open another tap. Use the tap that extends the farthest.
6. Keep track of taps used: Increment the tap count for each tap used. If the current `end` is greater than or equal to the total garden length `n`, we have successfully watered the entire garden and can return the tap count plus one.
7. Return result: If we've iterated through all intervals and haven't covered the entire garden, return -1, as it's not possible to water the garden completely.

### Time Complexity

The time complexity of the solution is dominated by the sorting step, which takes O(n log n) time. The subsequent iteration through the sorted intervals takes linear time O(n). Overall, the time complexity is O(n log n).

### Space Complexity

The space complexity is O(n) due to the storage of intervals and the constant space used for variables.

Feel free to explore the provided code in this repository to see the implementation in action.