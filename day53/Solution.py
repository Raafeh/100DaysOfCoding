from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Create a dictionary to store possible jump sizes for each stone
        jump_options = {stone: set() for stone in stones}
        jump_options[0].add(0)  # Frog starts at the first stone with jump size 0
        
        # Iterate through the stones
        for stone in stones:
            for jump in jump_options[stone]:
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in jump_options:
                        jump_options[stone + next_jump].add(next_jump)
        
        # If the last stone has any jump options, the frog can cross the river
        return bool(jump_options[stones[-1]])
s=Solution()

# Testcase 1:
print(s.canCross([0,1,3,5,6,8,12,17])) # True

# Testcase 2:
print(s.canCross([0,1,2,3,4,8,9,11])) # False

# Testcase 3:
print(s.canCross([0,2])) # False