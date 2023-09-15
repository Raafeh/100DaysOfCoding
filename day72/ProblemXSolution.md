# Minimum Cost to Connect Points


## Problem Description

You are given an array `points` representing integer coordinates of some points on a 2D plane, where `points[i] = [xi, yi]`. The cost of connecting two points `[xi, yi]` and `[xj, yj]` is defined as the Manhattan distance between them, which is given by the formula:

```
|xi - xj| + |yi - yj|
```

The task is to find the minimum cost to connect all points in such a way that there is exactly one simple path between any two points.

### Example 1

Input:
```
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
```

Output:
```
20
```

Explanation:
We can connect the points as shown above to get the minimum cost of 20. Notice that there is a unique path between every pair of points.

### Example 2

Input:
```
points = [[3,12],[-2,5],[-4,1]]
```

Output:
```
18
```

## Approach and Solution

To solve this problem, we use Kruskal's algorithm, a greedy algorithm for finding the Minimum Spanning Tree (MST) of a graph. In this case, the points represent the vertices of the graph, and the cost between two points is the weight of the edge between them. Kruskal's algorithm finds the MST with the minimum total weight.

The implementation follows these steps:

1. Calculate the Manhattan distance between all pairs of points and store them as edges with their corresponding costs.
2. Sort the edges by cost in ascending order.
3. Initialize each point as its own parent.
4. Iterate through the sorted edges, adding them to the minimum spanning tree if they connect two disjoint components (points).
5. Calculate and return the minimum cost to connect all points.

### Time Complexity
The time complexity of this solution is dominated by the sorting step, which takes O(E * log(E)) time, where E is the number of edges (which is proportional to the number of points). 

### Space Complexity
The space complexity is O(N), where N is the number of points, as we store the parent array to track connected components.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
