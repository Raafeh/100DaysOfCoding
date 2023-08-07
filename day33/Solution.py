from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
s=Solution()

# Testcase 1:
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)) # Output = True

# Testcase 2:
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)) # Output = False

# Testcase 3:
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60)) # Output = True