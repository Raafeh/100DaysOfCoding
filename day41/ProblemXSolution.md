# List Partitioning 

## Problem Description

Given the head of a linked list and a value `x`, the task is to partition the linked list such that all nodes with values less than `x` come before nodes with values greater than or equal to `x`. The original relative order of the nodes within each partition should be preserved.

### Example

**Input:**
```
head = [1, 4, 3, 2, 5, 2]
x = 3
```

**Output:**
```
[1, 2, 2, 4, 3, 5]
```

## Approach and Solution

The solution to this problem involves iterating through the given linked list and segregating the nodes into two separate partitions: one for nodes with values less than `x`, and another for nodes with values greater than or equal to `x`. After segregating the nodes, the two partitions are merged together while preserving their original order.


1. Initialize two dummy nodes: `less_than_x_dummy` and `greater_or_equal_dummy`, along with their corresponding tail pointers.

2. Traverse the original linked list using a pointer `current`.
   - If the value of the current node is less than `x`, append it to the `less_than_x` partition and update the `less_than_x_tail`.
   - Otherwise, append it to the `greater_or_equal` partition and update the `greater_or_equal_tail`.

3. After traversing the linked list, connect the `greater_or_equal` partition's tail to `None`, effectively ending that partition.

4. Connect the tail of the `less_than_x` partition to the head of the `greater_or_equal` partition.

5. Return the head of the merged linked list (`less_than_x_dummy.next`).

### Time Complexity

The solution iterates through the entire linked list once, which takes O(n) time, where n is the number of nodes in the linked list.

### Space Complexity

The solution uses a constant amount of extra space for the two dummy nodes and their tail pointers. Hence, the space complexity is O(1).

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!