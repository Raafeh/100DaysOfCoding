from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for i in range(len(gain)):
            height = altitude[i] + gain[i]
            altitude.append(height)
        return max(altitude)
    
S = Solution()

# Testcase 1:
print(S.largestAltitude([-5,1,5,0,-7])) # 1

# Testcase 2:
print(S.largestAltitude([-4,-3,-2,-1,4,3,2])) # 0

# Testcase 3:
print(S.largestAltitude([44,32,-9,24,99,-2,37,64,19,-52,19,5,3])) #308
