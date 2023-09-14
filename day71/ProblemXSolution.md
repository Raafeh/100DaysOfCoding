# Reconstruct Itinerary

## Problem Description

You are given a list of airline tickets where each ticket is represented as a pair of departure and arrival airports. The task is to use all the given tickets once and only once to reconstruct the itinerary, starting from "JFK." If there are multiple valid itineraries, the solution should return the one with the smallest lexical order when read as a single string.

### Example 1

Input:
```
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
```

Output:
```
["JFK","MUC","LHR","SFO","SJC"]
```

### Example 2

Input:
```
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
```

Output:
```
["JFK","ATL","JFK","SFO","ATL","SFO"]
```

## Approach and Solution 

The solution to this problem involves constructing a graph of airports and their destinations, sorting the destinations lexicographically for each source airport, and then performing a depth-first search (DFS) starting from "JFK" to find the itinerary.

1. Create a graph where keys are source airports and values are lists of target airports in lexical order.
2. Sort the target airports lexicographically for each source airport.
3. Initialize an empty list to store the final itinerary.
4. Implement a DFS function to visit all neighbors of the current airport recursively and add them to the itinerary.
5. Start the DFS from "JFK."
6. Reverse the itinerary to get the correct order.

### Time Complexity

The time complexity of this solution is O(N*log(N)), where N is the number of tickets. This complexity arises from sorting the target airports for each source airport. The DFS operation takes O(N) time in total.

### Space Complexity

The space complexity is O(N), where N is the number of tickets. This space is used to store the graph, the itinerary, and the function call stack during DFS.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
