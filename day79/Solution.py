class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Initialize pointers for s and t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move the pointer in s
            j += 1  # Always move the pointer in t
        return i == len(s)  # If all characters in s are found in t in order, return True

S = Solution()

# Testcsae 1:
print(S.isSubsequence("abc", "ahbgdc"))  # Output: True

# Testcsae 2:
print(S.isSubsequence("axc", "ahbgdc"))  # Output: False

# Testcsae 3:
print(S.isSubsequence("b", "c"))  # Output: False