class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        # Fill in the DP array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to cell (i, j) is the sum of paths from above and from the left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is stored in dp[m-1][n-1]
        return dp[m - 1][n - 1]
    
s = Solution()

# Testcase 1:
print(s.uniquePaths(3, 7)) # 28

# Testcase 2:
print(s.uniquePaths(3, 2)) # 3

# Testcase 3:
print(s.uniquePaths(7, 3)) # 28