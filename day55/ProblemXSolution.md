# Minimum Penalty Shop Closing Time


## Problem Description

Given a string `customers` representing customer arrivals at each hour in the format of 'Y' (customer arrives) or 'N' (no customer arrives), the goal is to determine the earliest hour at which the shop must be closed to incur a minimum penalty. The penalty is calculated based on the following rules:

- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.

The task is to find the optimal closing hour that results in the lowest penalty.

### Example
Input: "YYNY"
Output: 2
Explanation: Closing the shop at the 2nd hour results in the minimum penalty of 1.

## Approach and Solution 

The provided solution efficiently finds the optimal closing hour using the following approach:

1. Initialize `max_score` and `score` to keep track of the maximum net score and the current net score, respectively.
2. Initialize `best_hour` to keep track of the best closing hour that gives the maximum net score.
3. Iterate through the `customers` string using enumerate to keep track of the current hour index and the corresponding character ('Y' or 'N').
4. Update the `score` by incrementing it when a customer arrives ('Y') and decrementing it when no customer arrives ('N').
5. If the current `score` is greater than the current `max_score`, update `max_score` and set `best_hour` to the current index.
6. Finally, return `best_hour + 1` as the best closing hour.

## Time Complexity

The time complexity of the solution is O(n), where n is the length of the input string `customers`. This is because we iterate through the string once, performing constant-time operations in each iteration.

## Space Complexity

The space complexity of the solution is O(1), as the algorithm only uses a constant amount of extra space to store variables regardless of the input size.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!