from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calculate_time(speed):
            total_time = 0
            n = len(dist)
            for i in range(n - 1):
                total_time += (dist[i] + speed - 1) // speed  # Ceiling division to account for waiting time
            total_time += dist[-1] / speed
            return total_time

        n = len(dist)
        if hour <= n - 1:
            return -1

        # Binary search to find the minimum speed
        left, right = 1, 10**7
        while left < right:
            mid = left + (right - left) // 2
            time_taken = calculate_time(mid)
            if time_taken <= hour:
                right = mid
            else:
                left = mid + 1

        # Check if the upper bound (right) is valid or not
        if calculate_time(right) <= hour:
            return right
        else:
            return -1

# Test cases
solution = Solution()
print(solution.minSpeedOnTime([1, 3, 2], 6))   # Output: 1
print(solution.minSpeedOnTime([1, 3, 2], 2.7)) # Output: 3
print(solution.minSpeedOnTime([1, 3, 2], 1.9)) # Output: -1
