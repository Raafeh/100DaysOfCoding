from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x

        if target < 0:
            return -1

        left, current_sum, min_operations = 0, 0, float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                min_operations = min(min_operations, len(nums) - (right - left + 1))

        return min_operations if min_operations != float('inf') else -1

s = Solution()

# Testcase 1:
print(s.minOperations([1,1,4,2,3], 5))
# Output: 2

# Testcase 2:
print(s.minOperations([5,6,7,8,9], 4))
# Output: -1

# Testcase 3:
print(s.minOperations([3,2,20,1,1,3], 10))
# Output: 5