from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        
        return result

s = Solution()

# Testcase 1:
print(s.majorityElement([3,2,3])) # [3]

# Testcase 2:
print(s.majorityElement([1,1,1,3,3,2,2,2])) # [2,1]

# Testcase 3:
print(s.majorityElement([1])) # [1]