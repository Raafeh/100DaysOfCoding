from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]

S = Solution()

# Testcase 1:
print(S.maxUncrossedLines([1,4,2], [1,2,4])) # 2

# Testcase 2:
print(S.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])) # 3

# Testcase 3:
print(S.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])) # 2