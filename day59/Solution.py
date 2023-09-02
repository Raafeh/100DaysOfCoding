from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for word in dictionary:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)])

            dp[i] = min(dp[i], dp[i - 1] + 1)

        return dp[n]

s = Solution()

# Testcase 1:
print(s.minExtraChar("leetscode", ["leet", "leetcode", "code"])) # 1

# Testcase 2:
print(s.minExtraChar("applesandpears", ["apple", "pear"])) # 5

# Testcase 3:
print(s.minExtraChar("leetcode", ["lee", "code", "e"])) # 0
