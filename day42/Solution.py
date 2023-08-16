from collections import Counter
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Create a Counter for the first word in the list
        common_counter = Counter(words[0])

        # Iterate through the rest of the words and update the common_counter
        for word in words[1:]:
            word_counter = Counter(word)
            common_counter &= word_counter

        # Convert the common_counter into a list of characters
        result = []
        for char, count in common_counter.items():
            result.extend([char] * count)

        return result
s=Solution()

# Testcase 1:
print(s.commonChars(["bella","label","roller"]))
# Output: ["e","l","l"]

# Testcase 2:
print(s.commonChars(["cool","lock","cook"]))
# Output: ["c","o"]
