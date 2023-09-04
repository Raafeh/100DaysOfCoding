# Linked List Cycle 

## Problem Description

Given the head of a singly-linked list, determine if the linked list contains a cycle.

A cycle in a linked list occurs when there is a node in the list that can be reached again by continuously following the `next` pointer. The problem does not provide the position (`pos`) of the cycle, but we need to detect whether a cycle exists in the linked list.

## Example

**Input:**
```python
head = [3, 2, 0, -4]
head.next.next.next.next = head.next
```

**Output:**
```python
True
```

## Approach and Solution 

We can solve this problem using the Floyd's cycle detection algorithm, also known as the "tortoise and hare" algorithm. This algorithm uses two pointers moving at different speeds to detect cycles in the linked list:

1. Initialize two pointers, `slow` and `fast`, both initially pointing to the head of the linked list.

2. Move the `slow` pointer one step at a time, and the `fast` pointer two steps at a time.

3. If there is a cycle in the linked list, the `fast` pointer will eventually catch up to the `slow` pointer.

4. If there is no cycle, the `fast` pointer will reach the end of the list, and we return `False`.

5. If the `fast` and `slow` pointers meet during their traversal, we return `True` as there is a cycle in the linked list.


- **Time Complexity:** O(N), where N is the number of nodes in the linked list. In the worst case, the `fast` pointer will visit all nodes once.

- **Space Complexity:** O(1), as we are using only two pointers (`slow` and `fast`) regardless of the size of the linked list.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!