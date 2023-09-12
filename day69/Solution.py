class Solution:
    def minDeletions(self, s: str) -> int:
        # Step 1: Initialize a dictionary to count character frequencies
        char_freq = {}
        
        # Step 2: Count the frequency of each character
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Step 3: Initialize a set to keep track of unique frequencies
        unique_freq = set()
        
        # Step 4: Make frequencies unique and add them to the set
        deletions = 0
        for freq in char_freq.values():
            while freq in unique_freq:
                freq -= 1
                deletions += 1
            if freq > 0:
                unique_freq.add(freq)
        
        # Step 5: Calculate the total number of deletions needed
        return deletions
        
s = Solution()

# Testcase 1:
print(s.minDeletions("aab"))
# Output: 0

# Testcase 2:
print(s.minDeletions("aaabbbcc"))
# Output: 2

# Testcase 3:
print(s.minDeletions("ceabaacb"))
# Output: 2