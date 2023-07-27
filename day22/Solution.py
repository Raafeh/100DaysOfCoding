from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        
        while left < right:
            target = right - (right - left) // 2
            
            extra = 0
            for power in batteries:
                extra += min(power, target)
            
            if extra // n >= target:
                left = target
            else:
                right = target - 1
        
        return left

s=Solution()

# Test Case 1:
print(s.maxRunTime(3, [2, 2, 3])) # 2

# Test Case 2:
print(s.maxRunTime(2, [1,1,1,1])) # 2