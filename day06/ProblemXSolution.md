# All Nodes Distance K in Binary Tree

## Problem Description

Given the `root` of a binary tree, a `target` node, and an integer `k`, the task is to find all the nodes that have a distance of `k` from the `target` node. The solution should return an array of the values of these nodes in any order.

## Example
<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" alt="Binary Tree" width="350" height="300">

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
```
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

## Approach and Solution

The problem can be efficiently solved using a Depth-First Search (DFS) approach. Here is the step-by-step solution:

1. Build a `parent` dictionary: Traverse the binary tree using DFS and store the `parent` information for each node. This will help us track the `parent` nodes during the search.

2. Perform DFS from the `target` node: Start the DFS from the `target` node and keep track of the visited nodes and their distances from the `target`. If the distance is equal to `k`, add the node's value to the result array. If the distance is less than `k`, continue the search to the node's children and parent (if applicable), ensuring that each node is visited only once to avoid cycles.


The time complexity of the solution is O(N), where N is the number of nodes in the binary tree. This is because we perform a DFS traversal once to build the parent dictionary and another DFS traversal to find the nodes at distance k.

The space complexity of the solution is O(N) as well. The space is primarily used for the parent dictionary, which stores N nodes in the binary tree. Additionally, the visited set requires space proportional to the number of nodes visited during the DFS traversal.

