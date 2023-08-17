from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque()
        distance = [[float('inf')] * cols for _ in range(rows)]
        
        # Initialize the queue with 0s and update their distance to 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distance[i][j] = 0
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if distance[new_row][new_col] > distance[row][col] + 1:
                        distance[new_row][new_col] = distance[row][col] + 1
                        queue.append((new_row, new_col))
        
        return distance
s=Solution()

# Testcase 1:
print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]

# Testcase 2:
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]

# Testcase 3:
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1],[2,3,2]]