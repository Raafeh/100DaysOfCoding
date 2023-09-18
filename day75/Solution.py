from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list of tuples (soldier_sum, row_index)
        rows_with_soldier_sum = [(sum(row), index) for index, row in enumerate(mat)]
        
        # Sort the list based on soldier_sum and row_index
        rows_with_soldier_sum.sort(key=lambda x: (x[0], x[1]))
        
        # Extract the indices of the k weakest rows
        weakest_rows_indices = [index for _, index in rows_with_soldier_sum[:k]]
        
        return weakest_rows_indices
    
s = Solution()

# Testcase 1:
print(s.kWeakestRows(mat = [[1,1,0,0,0],
                            [1,1,1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0,0],
                            [1,1,1,1,1]], k = 3))
# Output: [2,0,3]

# Testcase 2:
print(s.kWeakestRows(mat = [[1,0,0,0],
                            [1,1,1,1],
                            [1,0,0,0],
                            [1,0,0,0]], k = 2))
# Output: [0,2]
