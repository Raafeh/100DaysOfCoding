from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == key:
                result.append(i)
                continue
            for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                if nums[j] == key:
                    result.append(i)
                    break
        return sorted(result)
    
s=Solution()

# Test Case:1
print(s.findKDistantIndices([1, 2, 3, 7, 5], 2, 3)) # Solution= [0,1,2,3,4]

# Test Case:2
print(s.findKDistantIndices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 5)) # Solution= [0,1,2,3,4,5,6,7,8,9]

# Test Case:3
print(s.findKDistantIndices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, 5)) # Solution= []