class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
    
        # XOR all characters in string s and t
        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)
        
        # Convert the final result back to a character
        return chr(result)

S = Solution()

# Testcase 1:
print(S.findTheDifference("abcd", "abcde")) # e

# Testcase 2:
print(S.findTheDifference("", "y")) # y

# Testcase 3:
print(S.findTheDifference("a", "aa")) # a