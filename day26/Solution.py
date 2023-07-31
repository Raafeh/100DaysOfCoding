class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # Create a DP table to store the minimum ASCII sum of deleted characters
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the first row and column with cumulative ASCII values
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        # Fill the DP table by comparing characters and calculating the minimum sum
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        
        return dp[m][n]
    
s=Solution()

# Testcase 1:
print(s.minimumDeleteSum("sea","eat")) # Output = 231

# Testcase 2:
print(s.minimumDeleteSum("delete","leet")) # Output = 403

# Testcase 3:
print(s.minimumDeleteSum("ccaccjp","fwosarcwge")) # Output = 1399