from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        left, right = 0, 10**6  # Binary search range

        def isPathPossible(maxEffort):
            # Helper function to check if a path is possible with a given max effort
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            queue = [(0, 0)]

            while queue:
                x, y = queue.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and abs(heights[nx][ny] - heights[x][y]) <= maxEffort:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

            return visited[rows - 1][cols - 1]

        while left < right:
            mid = (left + right) // 2
            if isPathPossible(mid):
                right = mid
            else:
                left = mid + 1

        return left
s = Solution()

# Testcase 1:
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
# Output: 2

# Testcase 2:
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
# Output: 1

# Testcase 3:
print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
# Output: 0