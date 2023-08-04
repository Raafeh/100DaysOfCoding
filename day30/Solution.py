from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a set for fast word lookup
        wordSet = set(wordDict)
        
        # Create a dynamic programming table to store intermediate results
        # dp[i] will be True if s[:i] can be segmented into words from the dictionary
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string is always present in the dictionary
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[:j] can be segmented and s[j:i] is in the wordDict, update dp[i] to True
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
s=Solution()

# Testcase 1:
print(s.wordBreak("leetcode", ["leet", "code"])) # True

# Testcase 2:
print(s.wordBreak("applepenapple", ["apple", "pen"])) # True

# Testcase 3:
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # False