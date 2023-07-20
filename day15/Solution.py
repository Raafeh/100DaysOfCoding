from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for i in asteroids:
            while s and i < 0 and s[-1]>0 :
                if abs(i) > s[-1]:
                    s.pop()
                elif abs(i) == s[-1]:
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(i)
        return s
s=Solution()

# Testcase 1:
print(s.asteroidCollision([5,10,-5]))
# Output: [5,10]

# Testcase 2:
print(s.asteroidCollision([8,-8]))
# Output: []

# Testcase 3:
print(s.asteroidCollision([10,2,-5]))
# Output: [10]