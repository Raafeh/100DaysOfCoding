from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

        return dp[0][n-1] >= 0

s=Solution()

# Test Case 1:
print(s.PredictTheWinner([1, 5, 2])) # False

# Test Case 2:
print(s.PredictTheWinner([1, 5, 233, 7])) # True

# Test Case 3:
print(s.PredictTheWinner([1, 1])) # True