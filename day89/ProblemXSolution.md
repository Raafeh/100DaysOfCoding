# Remove Colored Pieces if Both Neighbors are the Same Color

## Problem Description

Alice and Bob are playing a game with colored pieces arranged in a line. Each piece is colored either 'A' or 'B'. They take alternating turns removing pieces from the line, following specific rules:

- Alice can only remove a piece colored 'A' if both its neighbors are also 'A'. She cannot remove 'B' pieces.
- Bob can only remove a piece colored 'B' if both its neighbors are also 'B'. He cannot remove 'A' pieces.

The players cannot remove pieces from the edge of the line. If a player cannot make a move on their turn, they lose, and the other player wins.

You are given a string `colors` representing the initial state of the line of pieces. Determine if Alice can win the game if both players play optimally.

## Example

Input: `colors = "AAABABB"`
Output: `true`

Explanation:
- Alice moves first and removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.
- Bob cannot make a move on his turn.
- Alice wins, so the function returns `true`.

## Approach and Solution

To solve this problem, we can count the consecutive 'A's and 'B's in the input string while following the hint provided:
- If a group of `n` consecutive pieces has the same color, a player can take `n - 2` of those pieces if `n` is greater than or equal to 3.

Based on this counting strategy, the solution can be outlined as follows:

1. Initialize variables to keep track of Alice and Bob's scores.
2. Initialize counters for consecutive 'A's and 'B's.
3. Iterate through the `colors` string character by character:
    - If the current character is 'A', increment the 'A' counter and reset the 'B' counter. If the 'A' counter is greater than or equal to 3, increment Alice's score.
    - If the current character is 'B', increment the 'B' counter and reset the 'A' counter. If the 'B' counter is greater than or equal to 3, increment Bob's score.
4. Determine the winner based on Alice and Bob's scores. If Alice's score is greater, return `True`; otherwise, return `False`.

### Time Complexity
The time complexity of this solution is O(n), where n is the length of the `colors` string, because we iterate through the string once. 

### Space Complexity
The space complexity is O(1), as we use a constant amount of extra space to store variables and counters.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
