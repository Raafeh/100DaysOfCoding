from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
s=Solution()

# Testcase 1:
print(s.peakIndexInMountainArray([0,1,0]))
# Output: 1

# Testcase 2:
print(s.peakIndexInMountainArray([0,2,1,0]))
# Output: 1

# Testcase 3:
print(s.peakIndexInMountainArray([0,10,5,2]))
# Output: 1