# Maximum Running Time of N Computers

## Problem Description

You have n computers, and you are given an array `batteries` where the `i-th` element represents the number of minutes the `i-th` battery can run a computer. Initially, you can insert at most one battery into each computer. After that, at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. However, the batteries cannot be recharged.

Your task is to find the maximum number of minutes you can run all n computers simultaneously using the given batteries.

## Example

**Input:**
```
n = 2
batteries = [3, 3, 3]
```

**Output:**
```
4
```

**Explanation:**

Initially, insert battery 0 into the first computer and battery 1 into the second computer.

After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.

At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.

By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.

So, we can run the two computers simultaneously for at most 4 minutes, and that is the maximum time possible.

## Approach and Solution

To solve the problem efficiently, we can use binary search. We know that the maximum number of minutes we can run all n computers simultaneously is bounded between the minimum and maximum values in the `batteries` array. This is because, at any given time, the remaining runtime of the computers will be limited by the battery with the minimum remaining time.

We start the binary search with the range from 1 to the average of the total battery minutes per computer. Then, we iteratively check if it's possible to run all n computers for a given target time by simulating the process. For each battery, we use the minimum of its current remaining time and the target time to calculate the total available minutes for all computers.

If the total available minutes per computer are greater than or equal to the target, it means the target is achievable, and we update the left boundary of the binary search to move higher in the search space. Otherwise, we update the right boundary to move lower in the search space.

The binary search continues until the left and right boundaries meet, and the value of `left` represents the maximum number of minutes that can be achieved to run all n computers simultaneously.

## Time Complexity

The time complexity of the solution is O(n * log(T)), where n is the number of computers, and T is the total sum of minutes in the `batteries` array. The log(T) factor comes from the binary search.

## Space Complexity

The space complexity is O(1) as we only use a few variables for computation and don't use any additional data structures that grow with the input size.