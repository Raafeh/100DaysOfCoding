from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the array
        shortest_str = min(strs, key=len)
        
        # Iterate over the characters of the shortest string
        for i, char in enumerate(shortest_str):
            # Check if the current character is common among all strings
            for s in strs:
                if s[i] != char:
                    return shortest_str[:i]
        
        return shortest_str

solution = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""
