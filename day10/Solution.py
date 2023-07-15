from typing import List
class Solution:
    #  Class representing the solution for the problem
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        
        return True

s=Solution()
# Testcase 1:
print(s.check([3,4,5,1,2]))
# Output: True

# Testcase 2:
print(s.check([2,1,3,4]))
# Output: False

# Testcase 3:
print(s.check([1,2,3]))
# Output: True