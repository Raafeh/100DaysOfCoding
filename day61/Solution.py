from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move the slow pointer by one step
            fast = fast.next.next  # Move the fast pointer by two steps

            if slow == fast:
                return True  # If they meet, there is a cycle

        return False  # If we reach the end of the list, there is no cycle

s=Solution()

# Testcase 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
head=ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(-4)
head.next.next.next.next=head.next
print(s.hasCycle(head))

# Testcase 2:
# Input: head = [1,2], pos = 0
# Output: true
head=ListNode(1)
head.next=ListNode(2)
head.next.next=head
print(s.hasCycle(head))


