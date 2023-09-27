class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
    
        # Calculate the size of the decoded string without actually decoding it
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        
        # Traverse the string in reverse order to find the kth letter
        for char in reversed(s):
            k %= size  # Reduce k to its relative position in the current block
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                size /= int(char)
            else:
                size -= 1
S = Solution()

# Testcase 1:
print(S.decodeAtIndex("leet2code3", 10)) # o

# Testcase 2:
print(S.decodeAtIndex("ha22", 5)) # h

# Testcase 3:
print(S.decodeAtIndex("a2345678999999999999999", 1)) # a