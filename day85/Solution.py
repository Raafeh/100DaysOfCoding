from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        stack = []
        odds = []
        for n in nums:
            if n % 2 == 0:
                stack.append(n)
            else:
                odds.append(n)
        
        stack.extend(odds)

        return stack

S = Solution()

# Testcase 1:
print(S.sortArrayByParity([3,1,2,4]))

# Testcase 2:
print(S.sortArrayByParity([0]))

# Testcase 3:
print(S.sortArrayByParity([1,2,3,4,5,6,7,8,9,10]))