from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 2
                island.append((i, j))
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(i + dx, j + dy)

        n = len(grid)
        island = []
        found = False

        # Find and mark the first island (DFS)
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        queue = deque(island)
        level = 0

        # Use BFS to find the shortest path to the second island
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return level
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            queue.append((nx, ny))
            level += 1

s = Solution()

# Testcase 1:
print(s.shortestBridge([[0,1],[1,0]])) # 1

# Testcase 2:
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])) # 2

# Testcase 3:
print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])) # 1