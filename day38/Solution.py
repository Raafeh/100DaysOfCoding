from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting cell has an obstacle, there's no way to reach the destination
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize a 2D DP array to store the number of paths to each cell
        dp = [[0] * n for _ in range(m)]
        
        # Base case: there's one way to reach the starting cell
        dp[0][0] = 1
        
        # Fill in the DP array based on the obstacles and the previous paths
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # If there's an obstacle, set the paths to this cell as 0
                    dp[i][j] = 0
                else:
                    # If not an obstacle, add the paths from the cells above and left
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        
        # The result is the number of paths to the destination cell
        return dp[m - 1][n - 1]

s=Solution()

# Testcase 1:
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
# Output: 2

# Testcase 2:
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
# Output: 1

# Testcase 3:
print(s.uniquePathsWithObstacles([[1,0]]))
# Output: 0