# Combination Sum IV

## Problem Description

Given an array of distinct integers `nums` and a target integer `target`, your task is to determine the number of possible combinations that add up to the target.

**Example 1:**

Input: `nums = [1,2,3], target = 4`
Output: `7`
Explanation: The possible combination ways are:
- (1, 1, 1, 1)
- (1, 1, 2)
- (1, 2, 1)
- (1, 3)
- (2, 1, 1)
- (2, 2)
- (3, 1)

Note that different sequences are counted as different combinations.

**Example 2:**

Input: `nums = [9], target = 3`
Output: `0`

## Approach and Solution

To solve this problem efficiently, we can use a dynamic programming approach. We'll create a list `dp`, where `dp[i]` will store the number of combinations for a target value of `i`. We initialize `dp[0]` to 1 because there's one combination for a target of 0, which is an empty combination.

Then, we iterate through all possible target values from 1 to the given `target`. For each target value, we loop through the `nums` array and calculate the number of combinations for the current target by considering each number in `nums`. We update `dp[i]` by adding the number of combinations for the reduced target value (`i - num`) for each `num` in `nums`.

Finally, the last element of `dp` (`dp[target]`) will contain the number of combinations for the target.

### Time Complexity

The time complexity of this solution is O(target * len(nums)), where `target` is the given target value and `len(nums)` is the length of the `nums` array. We iterate through all possible target values from 1 to `target`, and for each target value, we iterate through the `nums` array.

### Space Complexity

The space complexity of this solution is O(target), as we use a list `dp` of size `target + 1` to store the number of combinations for each target value.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
