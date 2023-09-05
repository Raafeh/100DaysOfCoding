# Copy Linked List with Random Pointer

This repository provides a solution to the problem of creating a deep copy of a linked list that contains random pointers. The problem statement requires constructing a new linked list with exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointers of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

## Problem Description

Given a linked list of length `n`, each node contains an additional random pointer, which could point to any node in the list or be `null`. The goal is to construct a deep copy of the list and return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (ranging from 0 to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

### Examples

#### Example 1:

Input:
```
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

Output:
```
[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

#### Example 2:

Input:
```
head = [[1,1],[2,1]]
```

Output:
```
[[1,1],[2,1]]
```

#### Example 3:

Input:
```
head = [[3,null],[3,0],[3,null]]
```

Output:
```
[[3,null],[3,0],[3,null]]
```

## Approach and Solution 

To solve this problem, we can use a hash map to keep track of the mapping between original nodes and their corresponding copied nodes. Here's an overview of the solution:

1. Create a dictionary (hash map) to store the mapping between original nodes and copied nodes.

2. First pass: Traverse the original linked list and create a copy of each node. Map each original node to its corresponding copied node in the dictionary.

3. Second pass: Update the `next` and `random` pointers of the copied nodes using the mapping stored in the dictionary.

4. Return the head of the copied linked list.



- Time Complexity: O(N) - We perform two passes over the linked list, where N is the number of nodes in the list. In each pass, we perform constant-time operations.

- Space Complexity: O(N) - We use a dictionary to store the mapping between original nodes and copied nodes. In the worst case, when all nodes are unique, the space complexity is O(N).