# Check if Points Make a Straight Line

## Problem Description

You are given an array of coordinates, where each coordinate is represented as [x, y]. The task is to check if these points make a straight line in the XY plane.

### Example 1:
Input: `[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
Output: `true`

### Example 2:
Input: `[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
Output: `false`

## Approach and Solution

The solution to this problem involves checking whether all the given points lie on the same straight line. To achieve this, we can calculate the slope between the first two points and then compare the slopes between the first point and each of the remaining points. If all the slopes are equal, the points form a straight line.

1. Define a function `isSameLine` that checks if three points (x1, y1), (x2, y2), and (x3, y3) are collinear by comparing the slopes: `(x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)`.
2. Extract the coordinates of the first two points as (x1, y1) and (x2, y2).
3. Iterate through the remaining points, starting from the third point (index 2). For each point (x, y), use the `isSameLine` function to check if it lies on the same line as the first two points (x1, y1) and (x2, y2).
4. If any point is found not to lie on the same line as the first two points, return `False`.
5. If all points pass the test and are on the same line, return `True`.

### Time Complexity

The time complexity of this solution is O(n), where n is the number of points in the input array. We iterate through all the points once to check if they lie on the same line.

### Space Complexity

The space complexity of this solution is O(1) because we only use a constant amount of extra space for variables and calculations, regardless of the size of the input array.
