# Excel Sheet Column Title Conversion

## Problem Statement

Given an integer `columnNumber`, the task is to convert it into its corresponding Excel column title.

### Example

- Input: `columnNumber = 28`
  Output: `"AB"`
  
- Input: `columnNumber = 701`
  Output: `"ZY"`

## Approach and Solution 

To solve this problem, we can convert the given column number into its corresponding Excel column title using a systematic approach. Here's how the solution works:

1. Initialize an empty string `result` to store the final Excel column title.
2. Loop while the `columnNumber` is greater than 0:
   - Subtract 1 from `columnNumber` to create a 0-based index.
   - Calculate the remainder when dividing `columnNumber` by 26. This remainder will represent the current letter in the column title.
   - Convert the remainder to the corresponding letter using the ASCII value of 'A' and append it to the `result`.
   - Divide `columnNumber` by 26 to proceed to the next iteration.
3. Return the reversed `result` as the final Excel column title.


- Time Complexity: O(log N)
  The time complexity of the solution is determined by the number of iterations in the loop, which depends on the value of the `columnNumber`. Since we're dividing the `columnNumber` by 26 in each iteration, the number of iterations is logarithmic in base 26.

- Space Complexity: O(log N)
  The space complexity mainly accounts for the space needed to store the `result` string, which can grow logarithmically with the input `columnNumber`.

