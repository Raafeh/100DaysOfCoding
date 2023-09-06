# Split Linked List in Parts

## Problem Description

Given the head of a singly linked list and an integer `k`, your task is to split the linked list into `k` consecutive linked list parts. The length of each part should be as equal as possible, with no two parts differing in size by more than one node. The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

### Example 1:

**Input:**
```
head = [1,2,3], k = 5
```

**Output:**
```
[[1],[2],[3],[],[]]
```

### Example 2:

**Input:**
```
head = [1,2,3,4,5,6,7,8,9,10], k = 3
```

**Output:**
```
[[1,2,3,4],[5,6,7],[8,9,10]]
```

## Approach and Solution

To solve this problem, we follow these steps:

1. Find the length of the linked list by iterating through it.
2. Calculate the average size of each part and the number of parts that should have one extra node.
3. Iterate through the linked list again, splitting it into `k` parts, and updating the `result` array.
   - For each part, we determine its size based on the calculated average and extra nodes.
   - We maintain two pointers - `current` and `temp` - to split the list.
   - If a part is empty, we append `None` to the `result` array.
   - Otherwise, we append the head of the current part to the `result`, update the `current` pointer, and sever the connection to form the next part.

### Time Complexity

The time complexity of this solution is O(N), where N is the number of nodes in the linked list. We iterate through the list twice, first to find its length and second to split it into parts.

### Space Complexity

The space complexity is O(k), as we store the resulting linked list parts in an array of size `k`. In the worst case, when k is equal to the length of the linked list, this would be O(N). However, in practice, it is O(k).
