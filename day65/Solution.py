from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        # Initialize the result with the first row
        result = [[1]]

        # Generate the subsequent rows
        for i in range(1, numRows):
            # Generate a new row by summing the previous row
            prev_row = result[-1]
            new_row = [1]  # The first element is always 1
            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                new_row.append(new_element)
            new_row.append(1)  # The last element is always 1

            result.append(new_row)

        return result

s = Solution()

# Testcase 1:
print(s.generate(5))
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Testcase 2:
print(s.generate(1))
# Output: [[1]]

