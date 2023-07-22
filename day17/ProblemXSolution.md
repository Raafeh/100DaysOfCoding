# Knight Probability in Chessboard 

## Problem Statement

The problem involves a chessboard of size `n x n`, where a knight starts at a given cell `(row, column)` and attempts to make exactly `k` moves. The knight has eight possible moves it can make, and it chooses one of these moves uniformly at random during each step. The goal is to calculate the probability that the knight remains on the chessboard after making `k` moves.

<img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" alt="Binary Tree" width="300" height="300">

Given the following input parameters:
- `n`: The size of the `n x n` chessboard.
- `k`: The number of moves the knight will make.
- `row`, `column`: The starting position of the knight on the chessboard (0-indexed).

The task is to find the probability that the knight will still be on the chessboard after making exactly `k` moves.

## Example

Input:
- `n = 3`
- `k = 2`
- `row = 0`
- `column = 0`

Output:
- The probability that the knight remains on the board after `k` moves is `0.06250`.

Explanation:
- There are two moves (to `(1, 2)` and `(2, 1)`) that will keep the knight on the board from the starting position `(0, 0)`.
- From each of those positions, there are also two moves that will keep the knight on the board.
- The total probability the knight stays on the board is `0.0625`.

## Approach and Solution

To solve this problem efficiently, we use dynamic programming to calculate the probabilities of the knight being at each cell of the chessboard after a certain number of moves. We define a 3D table `dp` to keep track of these probabilities.

### Dynamic Programming Approach

1. We create a 3D table `dp`, where `dp[i][j][steps]` represents the probability that the knight is at position `(i, j)` on the chessboard after `steps` moves.

2. We set the base case `dp[row][column][0] = 1`, indicating that the knight starts at the given position with a probability of 1 for `steps = 0`.

3. Next, we iterate through the number of moves from `1` to `k`, and for each `step`, we update the probabilities for all cells on the chessboard based on the knight's possible moves.

4. For each position `(i, j)` on the chessboard and for each possible move, we calculate the new position `(r, c)` after making the move. If the new position `(r, c)` is still within the chessboard boundaries, we update `dp[i][j][steps]` by adding the probability of being at `(r, c)` after `steps - 1` moves, divided by 8.0 (since the knight can make 8 moves).

5. After completing the dynamic programming loop, the probability of the knight staying on the chessboard after `k` moves is the sum of probabilities in the `dp` table for all cells `(i, j)`.


The time complexity of the solution is O(n^2 * k) because we iterate through the `n x n` chessboard and for each cell, we calculate the probabilities for `k` steps.

The space complexity of the solution is O(n^2 * k) as well. The `dp` table requires `n^2 * k` space to store the probabilities for each cell and for each step.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!