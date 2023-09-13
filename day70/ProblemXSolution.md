# Candy 

## Problem Description

You are given an array of integer ratings representing the ratings of n children standing in a line. Each child is to be given candies based on the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating should receive more candies than their neighbors.

Your task is to determine the minimum number of candies needed to distribute to the children while satisfying the above conditions.

### Example

**Input:**

```python
ratings = [1, 0, 2]
```

**Output:**

```python
5
```

**Explanation:**

You can allocate candies as follows:
- The first child receives 2 candies.
- The second child receives 1 candy.
- The third child receives 2 candies.
Total candies needed = 2 + 1 + 2 = 5.

**Input:**

```python
ratings = [1, 2, 2]
```

**Output:**

```python
4
```

**Explanation:**

You can allocate candies as follows:
- The first child receives 1 candy.
- The second child receives 2 candies.
- The third child receives 1 candy.
Total candies needed = 1 + 2 + 1 = 4.

## Approach and Solution

To solve this problem efficiently, we can use a two-pass algorithm:

1. In the first pass, we traverse the `ratings` array from left to right. For each child, we compare their rating with the previous child. If their rating is higher, we give them one more candy than the previous child. This ensures that children with higher ratings get more candies than their left neighbors.

2. In the second pass, we traverse the `ratings` array from right to left. For each child, we again compare their rating with the next child. If their rating is higher, we make sure they have more candies than their right neighbor. We take the maximum of their current candy count and what is required to satisfy this condition.

Finally, we calculate the total number of candies needed by summing up the elements in the `candies` array, which holds the number of candies each child receives.

### Time Complexity

The time complexity of this solution is O(n) because we perform two passes through the `ratings` array, each taking linear time in the number of children, n.

### Space Complexity

The space complexity is O(n) as we create an additional `candies` array of the same size as the input `ratings` array to keep track of the number of candies each child receives.