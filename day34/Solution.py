from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=nums.index(min(nums))

        def binarySearch(lo,hi,target):
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if nums[mid]>target:
                    hi=mid-1
                elif nums[mid]<target:
                    lo=mid+1
                else:
                    return mid
            return -1
        
        if target>=nums[pivot] and target<=nums[len(nums)-1]:
            return binarySearch(pivot,len(nums)-1,target)
        else:
            return binarySearch(0,pivot,target)

s=Solution()

# Testcase 1:
print(s.search([4,5,6,7,0,1,2],0)) # 4

# Testcase 2:   
print(s.search([4,5,6,7,0,1,2],3)) # -1

# Testcase 3:
print(s.search([1],0)) # -1