# Counting Bits

## Problem Description

Given an integer `n`, you are required to return an array `ans` of length `n + 1` such that for each `i` (0 <= `i` <= `n`), `ans[i]` is the number of 1's in the binary representation of `i`. 

### Example

**Input**: `n = 5`
**Output**: `[0, 1, 1, 2, 1, 2]`

Explanation:
- 0 --> 0 (0 in binary)
- 1 --> 1 (1 in binary)
- 2 --> 1 (10 in binary)
- 3 --> 2 (11 in binary)
- 4 --> 1 (100 in binary)
- 5 --> 2 (101 in binary)

## Approach and Solution

The problem can be efficiently solved in linear time O(n) using a dynamic programming approach and bit manipulation.

1. Initialize an array `ans` to store the count of 1's for each number from 0 to `n`.

2. Loop from `i = 1` to `n` (inclusive):
   - Calculate `i >> 1` (right-shifted `i` by one position) to remove the rightmost bit from the binary representation of `i`.
   - To calculate the count of 1's for `i`, use the count of 1's for `i >> 1` and add 1 if `i` is odd, which is done using the expression `ans[i] = ans[i >> 1] + (i & 1)`.

3. The final `ans` array will contain the desired counts.

### Time Complexity

- Time Complexity: O(n) - The algorithm makes a single pass through the numbers from 1 to `n`, and each operation within the loop takes constant time.

### Space Complexity

- Space Complexity: O(n) - The space complexity is O(n) because we create an array of length `n + 1` to store the counts.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!