from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False
        
        return increasing or decreasing

S = Solution()

# Testcase 1:
print(S.isMonotonic([1,2,2,3])) # True

# Testcase 2:
print(S.isMonotonic([6,5,4,4])) # True

# Testcase 3:
print(S.isMonotonic([1,3,2])) # False