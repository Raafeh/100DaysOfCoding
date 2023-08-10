from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
    
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return True
            if nums[lo]==nums[mid]:
                lo+=1
                continue
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
                    
        return False

s=Solution()

# Testcase 1:
print(s.search([2,5,6,0,0,1,2],0)) # True

# Testcase 2:
print(s.search([2,5,6,0,0,1,2],3)) # False

# Testcase 3:
print(s.search([1,0,1,1,1],0)) # True