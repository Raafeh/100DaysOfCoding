# Maximum Length of Pair Chain


## Problem Description

Given an array of pairs where each pair represents an interval `[left, right]`, you need to find the length of the longest chain of pairs that can be formed such that each pair `[a, b]` follows the pair `[c, d]` if `b < c`.

## Example

**Input:**
```
pairs = [[1, 2], [7, 8], [4, 5]]
```

**Output:**
```
3
```

**Explanation:**
The longest chain is `[1, 2]` -> `[4, 5]` -> `[7, 8]`.

## Approach and Solution 

The problem requires finding the longest chain of pairs following a specific condition. This is a typical dynamic programming problem that can be solved using the following approach:

1. **Sort the Pairs**: To ensure that we can form a valid chain, we start by sorting the given pairs based on their end values. This sorting step helps us consider pairs in a sequence that would contribute to the longest chain.

2. **Dynamic Programming**: We use a dynamic programming (DP) approach to keep track of the length of the longest chain ending at each index. We initialize a DP array `dp` where each element represents the length of the longest chain ending at that index, initially set to 1.

3. **Iterative Comparison**: Starting from the second pair, we iterate through each pair and compare it with the previous pairs. If the end value of a previous pair is less than the start value of the current pair, we can extend the chain by including this pair. We update the DP value for the current index based on this comparison.

4. **Maximum Length**: Finally, we find and return the maximum value in the DP array. This value represents the length of the longest chain.

### Time Complexity

- Sorting the pairs takes O(n log n) time, where n is the number of pairs.
- The dynamic programming loop iterates over each pair, and for each pair, it iterates over all previous pairs. Hence, the time complexity of the dynamic programming step is O(n^2).

Overall, the time complexity of the solution is dominated by the sorting step, resulting in O(n log n) time complexity.

### Space Complexity

The space complexity of the solution is O(n), where n is the number of pairs. This is due to the space required to store the DP array.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!