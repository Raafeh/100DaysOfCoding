class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for i in range(1,n//2+1):
            if n % i == 0:
                pattern = s[:i] * (n//i)
                if s == pattern:
                    return True
             
        return False    
    
s=Solution()

# Testcase 1:
print(s.repeatedSubstringPattern("abab")) # True

# Testcase 2:
print(s.repeatedSubstringPattern("aba")) # False

# Testcase 3:
print(s.repeatedSubstringPattern("abcabcabcabc")) # True