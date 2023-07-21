from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp_lengths = [1] * n  # Length of the longest increasing subsequence ending at index i
        dp_counts = [1] * n   # Count of longest increasing subsequences ending at index i

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_lengths[j] + 1 > dp_lengths[i]:
                        dp_lengths[i] = dp_lengths[j] + 1
                        dp_counts[i] = dp_counts[j]
                    elif dp_lengths[j] + 1 == dp_lengths[i]:
                        dp_counts[i] += dp_counts[j]

        max_length = max(dp_lengths)
        ans = 0

        for length, count in zip(dp_lengths, dp_counts):
            if length == max_length:
                ans += count

        return ans

s=Solution()

# Testcase 1:
print(s.findNumberOfLIS([1,3,5,4,7]))
# Output: 2

# Testcase 2:
print(s.findNumberOfLIS([2,2,2,2,2]))
# Output: 5

# Testcase 3:
print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))
# Output: 3