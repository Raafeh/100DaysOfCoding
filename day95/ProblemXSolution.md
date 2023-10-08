# Finding Highest Altitude

## Problem Description

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `(0 <= i < n)`. The biker starts his trip on point 0 with an altitude equal to 0. The task is to find the highest altitude reached during the road trip.

### Example

**Input:**
```python
gain = [-5,1,5,0,-7]
```

**Output:**
```python
1
```

Explanation: The altitudes are `[0,-5,-4,1,1,-6]`. The highest is 1.

## Approach and Solution 

We can solve this problem by iteratively calculating the altitude at each point and keeping track of the highest altitude reached. Here's a step-by-step breakdown of the solution:

1. Initialize a list `altitude` with the first element set to 0, representing the starting altitude.
2. Iterate through the `gain` array using a for loop.
3. For each element in the `gain` array, calculate the new altitude by adding the gain to the previous altitude (the last element in the `altitude` list).
4. Append the new altitude to the `altitude` list.
5. After the loop is finished, use the `max` function to find the highest altitude from the `altitude` list.


### Time Complexity
The time complexity of this solution is O(n) because we iterate through the `gain` array once, where `n` is the length of the `gain` array.

### Space Complexity
The space complexity of this solution is O(n) as well. We create an additional list `altitude` to store the altitudes at each point, and the size of this list is proportional to the size of the input `gain` array.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
