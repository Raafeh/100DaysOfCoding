from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])  # Add a copy of the current combination to the result
                return

            for num in range(start, n + 1):
                path.append(num)  # Include the current number in the current combination
                backtrack(num + 1, path)  # Recur with the next start value
                path.pop()  # Backtrack and remove the last element to explore other combinations

        result = []
        backtrack(1, [])
        return result

s=Solution()

# Testcase 1:
print(s.combine(4,2)) # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# Testcase 2:
print(s.combine(1,1)) # Output: [[1]]

# Testcase 3:
print(s.combine(3,3)) # Output: [[1,2,3]]