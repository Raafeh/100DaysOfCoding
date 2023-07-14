from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}  
        for num in arr:
            prev = num - difference  
            if prev in dp:
                dp[num] = dp[prev] + 1
            else:
                dp[num] = 1

        return max(dp.values())

s=Solution()
# Testcase 1:
print(s.longestSubsequence([1,2,3,4],1))
# Output: 4

# Testcase 2:
print(s.longestSubsequence([1,3,5,7],1))
# Output: 1

# Testcase 3:
print(s.longestSubsequence([1,5,7,8,5,3,4,2,1],-2))
# Output: 4


