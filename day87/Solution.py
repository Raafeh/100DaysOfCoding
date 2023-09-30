from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        min_left = [0] * n
        min_left[0] = nums[0]
        
        # Find the minimum value to the left of each element
        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], nums[i])
        
        stack = []
        
        # Traverse the array from right to left
        for j in range(n - 1, -1, -1):
            if nums[j] > min_left[j]:
                # If nums[j] is greater than the minimum to its left, there's a possibility of a 132 pattern
                while stack and stack[-1] <= min_left[j]:
                    # Pop elements from the stack that are less than or equal to min_left[j]
                    stack.pop()
                
                if stack and stack[-1] < nums[j]:
                    # If there's an element in the stack that is less than nums[j], we found a 132 pattern
                    return True
                
                # Otherwise, push nums[j] onto the stack
                stack.append(nums[j])
        
        return False
S = Solution()

# Testcase 1:
print(S.find132pattern([1,2,3,4])) # False

# Testcase 2:
print(S.find132pattern([3,1,4,2])) # True

# Testcase 3:
print(S.find132pattern([-1,3,2,0])) # True