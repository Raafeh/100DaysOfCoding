class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        # If the lengths of s1 and s2 don't add up to the length of s3, it's not possible.
        if m + n != len(s3):
            return False
        
        # Create a DP array to store the interleave possibilities.
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: when both s1 and s2 are empty, s3 is also empty.
        dp[0][0] = True
        
        # Fill in the DP array using dynamic programming.
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        
        # The last cell in the DP array indicates whether s3 can be formed.
        return dp[m][n]
s=Solution()

# Testcase 1:
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# Output: True

# Testcase 2:
print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
# Output: False

# Testcase 3:
print(s.isInterleave("", "", ""))
# Output: True