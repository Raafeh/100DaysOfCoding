class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Initialize two dummy nodes for the two partitions
        less_than_x_dummy = ListNode()
        greater_or_equal_dummy = ListNode()
        less_than_x_tail = less_than_x_dummy
        greater_or_equal_tail = greater_or_equal_dummy
        
        # Traverse the original linked list
        current = head
        while current:
            if current.val < x:
                less_than_x_tail.next = current
                less_than_x_tail = current
            else:
                greater_or_equal_tail.next = current
                greater_or_equal_tail = current
            current = current.next
        
        # Connect the tails of the two partitioned linked lists to None
        greater_or_equal_tail.next = None
        less_than_x_tail.next = greater_or_equal_dummy.next
        
        return less_than_x_dummy.next

s=Solution()

# Testcase 1:
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
result = s.partition(head, x)
while result:
    print(result.val)
    result = result.next
# Output: 1 2 2 4 3 5