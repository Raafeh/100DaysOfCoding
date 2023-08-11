from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make amount 0, i.e., using no coins.

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

s=Solution()

# Testcase 1:
print(s.change(5,[1,2,5])) # Ans = 4

# Testcase 2:
print(s.change(3,[2])) # Ans = 0

# Testcase 3:
print(s.change(10,[10])) # Ans = 1