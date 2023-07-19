from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans=0
        k=float('-inf')
        for i in intervals:
            if i[0]>=k :
                k=i[1]
            else:
                ans+=1
        return ans
    
s=Solution()

# Testcase 1:
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

# Testcase 2:
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))

# Testcase 3:
print(s.eraseOverlapIntervals([[1,2],[2,3]]))