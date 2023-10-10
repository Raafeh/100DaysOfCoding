from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Check if two points are on the same line
        def isSameLine(x1, y1, x2, y2, x3, y3):
            return (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # Calculate the slope between the first two points
        # (x1, y1) and (x2, y2)
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Check if the current point is on the same line
            if not isSameLine(x1, y1, x2, y2, x, y):
                return False

        return True

s = Solution()

# Testcase 1:
print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # True

# Testcase 2:
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # False

# Testcase 3:
print(s.checkStraightLine([[1,1],[2,2]])) # True