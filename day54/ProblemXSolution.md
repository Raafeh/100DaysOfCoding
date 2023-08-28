# Implement Stack using Queues


## Problem Description

The goal is to implement a stack that supports the following operations:

- `push(x)`: Pushes element x to the top of the stack.
- `pop()`: Removes the element on the top of the stack and returns it.
- `top()`: Returns the element on the top of the stack.
- `empty()`: Returns true if the stack is empty, false otherwise.

The catch is that only standard operations of a queue are allowed, which includes push to back, peek/pop from front, size, and is empty operations.

## Approach and Solution 

The solution to this problem involves using two queues to simulate the behavior of a stack. The key idea is to maintain one queue as the "active" queue where new elements are pushed, while the other queue acts as a temporary buffer.

Here's how the solution works step by step:

1. Initialize two empty queues, `queue1` and `queue2`.

2. For the `push` operation:
   - If `queue1` is not empty, push the new element to `queue1`.
   - If `queue1` is empty, push the new element to `queue2`.

3. For the `pop` operation:
   - If `queue1` is not empty, move all elements from `queue1` to `queue2` except the last one. Then return and remove the last element from `queue1`.
   - If `queue1` is empty, do the same process with `queue2`.

4. For the `top` operation:
   - If `queue1` is not empty, return the last element from `queue1`.
   - If `queue1` is empty, return the last element from `queue2`.

5. For the `empty` operation:
   - Return `True` if both `queue1` and `queue2` are empty, otherwise return `False`.

### Time Complexity

- `push`: O(1)
- `pop`: O(n), where n is the number of elements in the non-empty queue (the queue containing the current stack elements).
- `top`: O(1)
- `empty`: O(1)

### Space Complexity

The space complexity of this implementation is O(n), where n is the total number of elements stored across both queues. This is because, at any given time, only one queue stores the stack elements, while the other queue acts as a buffer.


Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!