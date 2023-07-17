class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the order of digits using stacks
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        # Perform addition starting from the least significant digit
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create a new node with the current digit
            node = ListNode(total % 10)

            # Update the next pointer of the new node
            node.next = result
            result = node

        return result
s=Solution()

# Test Case 1
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = s.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)
# output: 7 8 0 7

# Test Case 2
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = s.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val)
# output: 8 0 7

# Test Case 3
l1 = ListNode(0)
l2 = ListNode(0)
result = s.addTwoNumbers(l1, l2)
print(result.val)
# output: 0