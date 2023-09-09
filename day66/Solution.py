from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        
        # There's one combination for target 0, which is an empty combination.
        dp[0] = 1
        
        # Iterate through all possible target values from 1 to target.
        for i in range(1, target + 1):
            for num in nums:
                # If the current target value minus the current number is greater than or equal to 0,
                # add the number of combinations for the reduced target to the current target's combinations.
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        # The last element of dp contains the number of combinations for the target.
        return dp[target]
    
s = Solution()

# Testcase 1:
print(s.combinationSum4([1, 2, 3], 4))
# Output: 7

# Testcase 2:
print(s.combinationSum4([9], 3))
# Output: 0

# Testcase 3:
print(s.combinationSum4([1, 2, 3], 32))
# Output: 181997601