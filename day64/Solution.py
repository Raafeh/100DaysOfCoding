# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prev = dummy
        curr = head
        
        # Move prev and curr to the correct positions
        for _ in range(left - 1):
            prev = prev.next
            curr = curr.next
        
        # Reverse the portion of the list from left to right
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next

s = Solution()