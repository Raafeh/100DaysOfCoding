# Minimum Speed to arrive on time

## Problem Description

You are given a floating-point number `hour`, which represents the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. You are also given an integer array `dist` of length `n`, where `dist[i]` describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

The task is to find the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time. If it is impossible to be on time, return -1.

### Example

**Input:** 
```
dist = [1, 3, 2]
hour = 6
```

**Output:** 
```
1
```

**Explanation:** 
- At speed 1:
  - The first train ride takes 1/1 = 1 hour.
  - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
  - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
  - You will arrive exactly at the 6 hour mark.

## Approach and Solution

To solve this problem, we use a binary search algorithm to find the minimum speed that satisfies the condition. The binary search algorithm is efficient because it helps narrow down the search space to find the optimal speed in logarithmic time.

1. Define a helper function `calculate_time(speed)` to calculate the total time taken to reach the office at a given speed. The function iterates through the train distances and calculates the time using ceiling division to account for the waiting time at each train ride.

2. Initialize the lower bound (`left`) as 1 (since the speed cannot be less than 1 km/hr) and the upper bound (`right`) as a large value, such as 10^7, as specified in the problem.

3. Check if the given hour is less than or equal to `n - 1` (number of trains minus one). If it is, then it's impossible to reach the office on time, so return -1.

4. Perform the binary search in the range `[left, right]`. At each step, calculate the time taken to reach the office at the current speed (mid). If the time is less than or equal to the given hour, update the upper bound (`right`) to the current speed and continue the binary search in the lower half. If the time is greater than the given hour, continue the binary search in the upper half.

5. After the binary search, check if the speed at the upper bound (`right`) is valid. If the calculated time at this speed is less than or equal to the given hour, return this speed as the minimum speed. Otherwise, return -1, indicating that it's impossible to reach the office on time.

### Time Complexity

The time complexity of the solution is O(log n) due to the binary search, where n is the number of trains.

### Space Complexity

The space complexity is O(1) as we are using a constant amount of extra space regardless of the input size.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!