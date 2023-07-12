# Find Eventual Safe States

## Problem Description

You are given a directed graph with `n` nodes, where each node is labeled from 0 to `n - 1`. The graph is represented by a 0-indexed 2D integer array `graph`, where `graph[i]` is an integer array of nodes adjacent to node `i`. Each entry `graph[i][j]` represents a directed edge from node `i` to node `graph[i][j]`.

A node is considered a terminal node if there are no outgoing edges from it. A node is considered a safe node if every possible path starting from that node leads to either a terminal node or another safe node.

You are required to find all the safe nodes in the graph and return them in ascending order.

## Example

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" alt="Binary Tree" width="500" height="150">

**Input:**
```
graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
```

**Output:**
```
[2, 4, 5, 6]
```

**Explanation:**
The given graph is represented as follows:

```
   0 -> 1 -> 2 -> 5
   ↓    ↓    ↓
   3    2    4
         ↓
         5
         ↓
         6
```

Nodes 5 and 6 are terminal nodes since there are no outgoing edges from them. Every path starting from nodes 2, 4, 5, and 6 leads to either node 5 or node 6. Hence, the safe nodes are [2, 4, 5, 6].

## Solution

To solve the problem, we can use a depth-first search (DFS) approach along with coloring to mark the state of each node. We can define three states for each node:

- **0 (White)**: Represents an unvisited node.
- **1 (Gray)**: Represents a node being visited or currently in the DFS path.
- **2 (Black)**: Represents a safe node.

We'll start with initializing all nodes to the White state (0). Then, we'll iterate over each node and perform a DFS from that node. During the DFS, we'll color the nodes as Gray (1) when we visit them and as Black (2) when we determine that they are safe. If we encounter a Gray node during the DFS, it means there is a cycle in the graph, and we won't mark any nodes in the cycle as safe.

After the DFS for all nodes, we'll collect all the safe nodes (Black) and return them in ascending order.

## Algorithm

1. Initialize an empty list `safeNodes` to store the safe nodes.
2. Initialize an empty list `color` to track the state of each node. Initially, set all nodes to 0 (White).
3. Define a helper function `isSafe` that takes a node index as input and returns True if the node is safe (Black), and False otherwise.
4. Iterate over each node index `i` from 0 to `n - 1`, where `n` is the number of nodes in the graph.
    - If `i` is safe (i.e., `isSafe(i)` returns True), append `i` to `safeNodes` and continue to the next iteration.
    - Otherwise, perform a DFS from node `i`:
        - If `i` is already visited (Gray), return False to break the cycle.
        - Color node `i` as Gray (1) to mark it as visited.
        - Iterate over each neighbor `neighbor` of node `i` in the graph.
            - Recursively call the DFS function on `neighbor`. If it returns False, return False.
        - Color node `i` as Black (2) to mark it as safe.
        - Return True.
5. Return `safeNodes` sorted in ascending order.


The time complexity for this solution is O(V + E), where V is the number of nodes (vertices) in the graph and E is the number of edges in the graph. In the worst-case scenario, we may have to visit every node and traverse every edge.

The space complexity is O(V), where V is the number of nodes in the graph. We use the `color` list to store the state of each node, which requires space proportional to the number of nodes.

