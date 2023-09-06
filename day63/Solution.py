# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the number of nodes in each part
        avg_size, extra_nodes = divmod(length, k)
        
        # Split the linked list into k parts
        result = []
        current = head
        for i in range(k):
            part_size = avg_size + 1 if i < extra_nodes else avg_size
            if part_size == 0:
                result.append(None)
            else:
                result.append(current)
                for j in range(part_size - 1):
                    current = current.next
                temp = current.next
                current.next = None
                current = temp
        
        return result

s = Solution()

# Testcase 1:
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
head = ListNode(1, ListNode(2, ListNode(3)))
k = 5
result = s.splitListToParts(head, k)
for i in range(len(result)):
    current = result[i]
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Testcase 2:
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
k = 3
result = s.splitListToParts(head, k)
for i in range(len(result)):
    current = result[i]
    while current:
        print(current.val, end=" ")
        current = current.next
    print()
    