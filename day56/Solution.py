from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]  
        ans = 0  
        # Traverse the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > last:  
                t = nums[i] // last  
                if nums[i] % last:
                    t += 1  
                last = nums[i] // t  
                ans += t - 1  
            else:
                last = nums[i]  
        return ans  
    
s=Solution()

# Testcase 1:
print(s.minimumReplacement([5, 2, 6, 1]))

# Testcase 2:
print(s.minimumReplacement([10, 1, 5, 6]))

# Testcase 3:
print(s.minimumReplacement([1, 2, 3, 4, 5]))