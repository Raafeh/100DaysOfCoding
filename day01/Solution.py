from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

# Test Case:1 
s = Solution() 
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # Solution= 2

# Test Case:2
print(s.minSubArrayLen(4, [1,4,4])) # Solution= 1

# Test Case:3
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # Solution= 0