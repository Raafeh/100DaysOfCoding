class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800: 
            return 1.0
        n = (n + 24) // 25
        memo = dict()
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i <= 0 and j <= 0: 
                return 0.5
            if i <= 0: 
                return 1.0
            if j <= 0: 
                return 0.0
            memo[(i, j)] = 0.25 * (dp(i - 4, j) + dp(i - 3, j - 1) + dp(i - 2, j - 2) + dp(i - 1, j - 3))
            return memo[(i, j)]
        
        return dp(n, n)
s=Solution()

# Testcase 1:
print(s.soupServings(50)) # Ans = 0.625

# Testcase 2:
print(s.soupServings(100)) # Ans = 0.71875

# Testcase 3:
print(s.soupServings(200)) # Ans = 0.796875