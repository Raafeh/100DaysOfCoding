class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create dictionaries to store character frequencies
        ransomNote_freq = {}
        magazine_freq = {}
        
        # Count frequencies in ransomNote
        for char in ransomNote:
            ransomNote_freq[char] = ransomNote_freq.get(char, 0) + 1
        
        # Count frequencies in magazine
        for char in magazine:
            magazine_freq[char] = magazine_freq.get(char, 0) + 1
        
        # Check if ransomNote can be constructed
        for char, count in ransomNote_freq.items():
            if char not in magazine_freq or count > magazine_freq[char]:
                return False
        
        return True

s = Solution()

# Testcase 1:
print(s.canConstruct("a", "b")) # False

# Testcase 2:
print(s.canConstruct("aa", "ab")) # False

# Testcase 3:
print(s.canConstruct("aa", "aab")) # True