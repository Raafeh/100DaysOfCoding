from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Initialize candies array with all 1s

        # First pass: Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: Traverse from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Calculate the total number of candies needed
        total_candies = sum(candies)
        return total_candies
s = Solution()

# Testcase 1:
print(s.candy([1,0,2]))
# Output: 5

# Testcase 2:
print(s.candy([1,2,2]))
# Output: 4