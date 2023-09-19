from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        # Move slow and fast pointers until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the entrance to the cycle (the repeated number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
s = Solution()

# Testcase 1:
print(s.findDuplicate([1,3,4,2,2]))
# Output: 2

# Testcase 2:
print(s.findDuplicate([3,1,3,4,2]))
# Output: 3

# Testcase 3:
print(s.findDuplicate([1,1]))
# Output: 1