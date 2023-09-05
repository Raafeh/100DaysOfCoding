from typing import Optional
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Create a mapping between original nodes and copied nodes using a dictionary
        mapping = {}
        
        # First pass: Create a copy of each node and map the original node to its copy
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # Second pass: Update the next and random pointers of the copied nodes
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next
        
        # Return the head of the copied linked list
        return mapping[head]

s=Solution()

# Testcase 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

print(s.copyRandomList(head))
