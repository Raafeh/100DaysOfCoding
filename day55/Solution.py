class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float('inf')
        best_closing_hour = -1
        
        for closing_hour in range(n + 1):
            penalty = 0
            for i in range(n):
                if (closing_hour < n and i >= closing_hour) or (closing_hour == n and customers[i] == 'Y'):
                    penalty += 1
                elif customers[i] == 'N':
                    penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                best_closing_hour = closing_hour
        
        return best_closing_hour

solution = Solution()

# Testcase 1:
print(solution.bestClosingTime("YYNY"))  # Output: 2

# Testcase 2:
print(solution.bestClosingTime("NNNNN"))  # Output: 0

# Testcase 3:
print(solution.bestClosingTime("YYYY"))  # Output: 4
