import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

s=Solution()

# Testcase 1:
print(s.findKthLargest([3,2,1,5,6,4],2)) # 5

# Testcase 2:
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4)) # 4

# Testcase 3:
print(s.findKthLargest([1],1)) # 1