from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        end = nums[0]
        
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start = end = num
        
        # Add the last range
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        
        return ranges

s = Solution()

# Testcase 1:
print(s.summaryRanges([0,1,2,4,5,7])) # Output: ["0->2","4->5","7"]

# Testcase 2:
print(s.summaryRanges([0,2,3,4,6,8,9])) # Output: ["0","2->4","6","8->9"]
