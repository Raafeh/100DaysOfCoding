from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums) - 1:
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recurse on the next position
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo the swap)

        result = []
        backtrack(0)
        return result
    
s=Solution()

# Testcase 1:
print(s.permute([1,2,3])) # Expected Output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Testcase 2:
print(s.permute([0,1])) # Expected Output = [[0,1],[1,0]]

# Testcase 3:
print(s.permute([1])) # Expected Output = [[1]]