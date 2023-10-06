class Solution:
    def integerBreak(self, n: int) -> int:
        # Initialize a list to store the maximum product for each number from 2 to n
        dp = [0] * (n + 1)

        # Base case: dp[2] = 1 since 2 can only be broken into 1 + 1
        dp[2] = 1

        # Calculate the maximum product for each number from 3 to n
        for i in range(3, n + 1):
            # Try breaking i into two parts: j and i - j
            # For each j from 1 to i // 2, calculate the product and update dp[i]
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

        # The result is stored in dp[n]
        return dp[n]

S = Solution()

# Testcase 1:
print(S.integerBreak(2))

# Testcase 2:
print(S.integerBreak(10))

# Testcase 3:
print(S.integerBreak(20))