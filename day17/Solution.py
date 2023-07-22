class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible moves of a knight
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        
        # Initialize the DP table
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        dp[row][column][0] = 1
        
        # Dynamic programming
        for steps in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for move in moves:
                        r, c = i + move[0], j + move[1]
                        if 0 <= r < n and 0 <= c < n:
                            dp[i][j][steps] += dp[r][c][steps - 1] / 8.0
        
        # Calculate the total probability of staying on the board
        probability = sum(dp[i][j][k] for i in range(n) for j in range(n))
        return probability

s=Solution()

# Testcase 1
print(s.knightProbability(3,2,0,0))
# Output: 0.0625

# Testcase 2
print(s.knightProbability(1,0,0,0))
# Output: 1.0

# Testcase 3
print(s.knightProbability(8,30,6,4))
# Output: 0.00019
