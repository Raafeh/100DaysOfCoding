from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        
        # Populate the dictionary
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
        
        result = []
        
        # Iterate through the dictionary to form groups
        for size, people in groups.items():
            while len(people) >= size:
                result.append(people[:size])
                people = people[size:]
        
        return result
    
s = Solution()

# Testcase 1:
print(s.groupThePeople([3,3,3,3,3,1,3]))
# Output: [[5],[0,1,2],[3,4,6]]

# Testcase 2:
print(s.groupThePeople([2,1,3,3,3,2]))
# Output: [[1],[0,5],[2,3,4]]

# Testcase 3:
print(s.groupThePeople([1]))
# Output: [[0]]