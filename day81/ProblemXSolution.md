# Sign of the Product of an Array

## Problem Description

You are given an integer array `nums`. Your task is to find the sign of the product of all values in the array using the `signFunc` function, which returns:
- 1 if `x` is positive.
- -1 if `x` is negative.
- 0 if `x` is equal to 0.

### Examples

**Example 1:**

Input: `nums = [-1, -2, -3, -4, 3, 2, 1]`

Output: `1`

Explanation: The product of all values in the array is 144, and `signFunc(144)` returns 1.

**Example 2:**

Input: `nums = [1, 5, 0, 2, -3]`

Output: `0`

Explanation: The product of all values in the array is 0, and `signFunc(0)` returns 0.

**Example 3:**

Input: `nums = [-1, 1, -1, 1, -1]`

Output: `-1`

Explanation: The product of all values in the array is -1, and `signFunc(-1)` returns -1.

## Approach and Solution

To solve this problem, we can follow these steps in our Python code:

1. Define a `signFunc` function that takes an integer `x` and returns the sign according to the rules provided.
2. Create a function `arraySign` that takes an array `nums` as input.
3. Initialize a variable `product` to 1 to store the product of all values in the `nums` array.
4. Iterate through the `nums` array, multiplying each element with the `product`.
5. After calculating the product, apply the `signFunc` to the product to determine the sign.
6. Return the sign as the output.

The Python code provided in this repository implements the above algorithm and provides solutions for the given examples.

### Time Complexity

The time complexity of this solution is O(n), where n is the number of elements in the `nums` array. This is because we iterate through the array once to calculate the product.

### Space Complexity

The space complexity is O(1) because we use a constant amount of extra space to store the `product` variable and the `signFunc` function doesn't use any additional memory based on the size of the input.
