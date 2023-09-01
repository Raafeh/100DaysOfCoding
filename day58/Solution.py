from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

s = Solution()

# Testcase 1:
print(s.countBits(2)) # [0,1,1]

# Testcase 2:
print(s.countBits(5)) # [0,1,1,2,1,2]

# Testcase 3:
print(s.countBits(8)) # [0,1,1,2,1,2,2,3,1]