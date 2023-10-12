class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the two strings are different, they can't be anagrams.
        if len(s) != len(t):
            return False

        # Create a dictionary to count the occurrences of each character in string s.
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Iterate through string t and decrement the counts in the dictionary.
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                # If the count becomes zero, remove the character from the dictionary.
                if char_count[char] == 0:
                    del char_count[char]
            else:
                # If a character in t is not in the dictionary, it's not an anagram.
                return False

        # If the dictionary is empty, it means all characters in s and t canceled out.
        return not bool(char_count)

S = Solution()

# Testcase 1:
print(S.isAnagram("anagram", "nagaram")) # True

# Testcase 2:
print(S.isAnagram("rat", "car")) # False

# Testcase 3:
print(S.isAnagram("a", "ab")) # False