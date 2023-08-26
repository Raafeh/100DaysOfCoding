from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort the pairs by the end value
        
        n = len(pairs)
        dp = [1] * n  # Initialize an array to store the length of longest chain ending at each index
        
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)  # Update the longest chain length
            
        return max(dp)  # Return the maximum value in the dp array

s=Solution()

# Testcase 1:
print(s.findLongestChain([[1,2], [2,3], [3,4]])) # 2

# Testcase 2:
print(s.findLongestChain([[1,2], [7,8], [4,5]])) # 3

# Testcase 3:
print(s.findLongestChain([[1,2], [2,3], [3,4], [4,5]])) # 2