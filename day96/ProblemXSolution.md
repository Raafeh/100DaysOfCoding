# Summary Ranges

## Problem Description

Given a sorted unique integer array `nums`, the task is to find the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range should be represented as follows:

- If a range consists of a single number, it should be represented as "a" (e.g., "5").
- If a range consists of multiple consecutive numbers, it should be represented as "a->b" (e.g., "2->4").

### Example 1:

Input: `nums = [0,1,2,4,5,7]`
Output: `["0->2","4->5","7"]`
Explanation: The ranges are:
- [0,2] --> "0->2"
- [4,5] --> "4->5"
- [7,7] --> "7"

### Example 2:

Input: `nums = [0,2,3,4,6,8,9]`
Output: `["0","2->4","6","8->9"]`
Explanation: The ranges are:
- [0,0] --> "0"
- [2,4] --> "2->4"
- [6,6] --> "6"
- [8,9] --> "8->9"

## Approach and Solution

To solve this problem, we can iterate through the `nums` array while keeping track of the start and end of each range. Here's how the solution works:

1. Initialize an empty list `ranges` to store the result.
2. Initialize two variables, `start` and `end`, to the first element of `nums`.
3. Iterate through the `nums` array, starting from the second element.
4. If the current number is consecutive to the previous number (i.e., `num == end + 1`), update the `end` variable to the current number.
5. If the current number is not consecutive, add the current range representation (either "a" or "a->b") to the `ranges` list and update the `start` and `end` variables to the current number.
6. After the loop, add the last range to the `ranges` list.
7. Finally, return the `ranges` list containing the summary ranges.

### Time Complexity
The time complexity of this solution is O(n), where n is the number of elements in the `nums` array, because we iterate through the array once. 

### Space Complexity
The space complexity is O(1) because we only use a constant amount of extra space to store the `ranges` list, `start`, and `end` variables.
