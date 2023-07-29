# Soup Serving Probability Problem

## Problem Description

You are given two types of soup: type A and type B. Initially, you have n ml of each type of soup. There are four kinds of operations:

1. Serve 100 ml of soup A and 0 ml of soup B.
2. Serve 75 ml of soup A and 25 ml of soup B.
3. Serve 50 ml of soup A and 50 ml of soup B.
4. Serve 25 ml of soup A and 75 ml of soup B.

Each turn, you will choose from the four operations with an equal probability of 0.25. If the remaining volume of soup is not enough to complete the operation, you will serve as much as possible. The process stops once you no longer have some quantity of both types of soup.

Your task is to calculate the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

## Example

### Input:
```
n = 50
```

### Output:
```
0.62500
```

Explanation:
- If we choose the first two operations, A will become empty first.
- For the third operation, A and B will become empty at the same time.
- For the fourth operation, B will become empty first.
- The total probability of A becoming empty first plus half the probability that A and B become empty at the same time is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

## Approach and Solution

The correct solution to the problem uses a top-down dynamic programming approach with memoization to efficiently compute the probability. It also adjusts the input parameter `n` to reduce the recursion depth and avoid stack overflow for large `n`.

Here is the outline of the correct solution:

1. If `n` is greater than 4800, return 1.0 since A is very likely to become empty first due to the large amount of soup.
2. Adjust `n` by dividing it by 25 and rounding up, making the recursion depth manageable.
3. Create a memoization dictionary to store previously computed results to avoid redundant calculations.
4. Implement a recursive function `dp(i, j)` that calculates the probability that A will be empty first given i ml of soup A and j ml of soup B remaining.
5. The base cases for the recursion are:
   - If both i and j are non-positive, return 0.5 since A and B have the same remaining volume, and the probability is equal.
   - If i is non-positive, return 1.0 since A is already empty.
   - If j is non-positive, return 0.0 since B is already empty.
6. In the recursive function, check if the result for the current state (i, j) is already computed in the memoization dictionary. If yes, return the stored result.
7. Otherwise, calculate the probability using the given operations and store the result in the memoization dictionary for future use.
8. Call the recursive function with the adjusted `n` and return the final result.

## Time Complexity

The time complexity of the correct solution is O(n^2) due to the recursion and memoization. However, the adjusted input parameter `n` significantly reduces the recursion depth and improves the efficiency of the algorithm.

## Space Complexity

The space complexity of the correct solution is also O(n^2) due to the memoization dictionary, which stores the results for each state (i, j) during the recursion.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!