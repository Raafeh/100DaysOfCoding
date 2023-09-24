from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product = product * n

        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1 
            else:
                return 0 

        return signFunc(product)

S = Solution()

# Testcase 1:
print(S.arraySign([-1,-2,-3,-4,3,2,1])) # 1

# Testcase 2:
print(S.arraySign([1,5,0,2,-3])) # 0

# Testcase 3:
print(S.arraySign([-1,1,-1,1,-1])) # -1

