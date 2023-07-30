class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # Create a 2D DP array to store the minimum number of turns for substrings.
        dp = [[0] * n for _ in range(n)]

        # Iterate through the string in reverse order.
        for i in range(n - 1, -1, -1):
            # Base case: A single character always requires one turn.
            dp[i][i] = 1

            for j in range(i + 1, n):
                # If the characters at both ends are the same, we can reduce the problem size by 1.
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    # Initialize dp[i][j] with the worst case (maximum) value.
                    dp[i][j] = j - i + 1

                    # Try every possible break point to minimize the turns.
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        # The answer is stored in dp[0][n - 1], representing the minimum turns for the whole string.
        return dp[0][n - 1]

s=Solution()

# Testcase 1:
print(s.strangePrinter("aaabbb")) # 2

# Testcase 2:
print(s.strangePrinter("aba")) # 2
