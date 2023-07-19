# Non-Overlapping Intervals

This repository contains a solution to the problem of finding the minimum number of intervals that need to be removed to make the rest of the intervals non-overlapping. The problem is defined as follows:

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, the goal is to determine the minimum number of intervals that need to be removed to ensure that the remaining intervals do not overlap.

## Example

**Input:**
```
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

**Output:**
```
1
```

**Explanation:**
By removing the interval `[1,3]`, the rest of the intervals `[1,2],[2,3],[3,4]` become non-overlapping.

## Approach and Solution

To solve the problem, we can use the following approach:

1. Sort the intervals based on the end time in ascending order. This ensures that the intervals with earlier end times come first.
2. Initialize a variable `count` to keep track of the number of intervals to be removed.
3. Initialize a variable `end` to store the end time of the first interval in the sorted array.
4. Iterate through the sorted intervals starting from the second interval:
   - If the start time of the current interval is less than `end`, it means there is an overlap. Increment `count` by 1.
   - Otherwise, update `end` to the end time of the current interval.
5. Return the value of `count`.

The time complexity of this solution is O(n log n), where n is the number of intervals. The complexity arises from the sorting step. The space complexity is O(1) since we only use a constant amount of additional space to store the variables `count` and `end`.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!

