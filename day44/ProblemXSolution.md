# Maximal Network Rank 


## Problem Description

You are given an infrastructure of n cities with some roads connecting these cities. Each road is bidirectional, connecting two different cities. The network rank of two different cities is defined as the total number of directly connected roads to either city. However, if a road is directly connected to both cities, it is only counted once. The goal is to find the maximal network rank of the entire infrastructure.

### Example

**Input:**
```
n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
```

**Output:**
```
4
```

Explanation: The network rank of cities 0 and 1 is 4, as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

## Approach and Solution 

1. Create a dictionary where each city number is a key, and the value is a set of cities directly connected to that city.
2. Iterate through the given roads and populate the dictionary based on the connections.
3. For every pair of cities, calculate the network rank by summing up the sizes of the sets of directly connected cities for both cities. If there's a direct road between the two cities, subtract 1 to avoid double counting.
4. Update the maximum network rank with the calculated network rank for each pair.
5. Return the maximum network rank as the result.

### Time Complexity

The solution involves iterating through all pairs of cities and calculating the network rank for each pair. Therefore, the time complexity of the solution is O(n^2), where n is the number of cities.

### Space Complexity

The space complexity is determined by the space used to store the dictionary of connections. Since each city can have connections to other cities, the space complexity is O(n), where n is the number of cities.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!