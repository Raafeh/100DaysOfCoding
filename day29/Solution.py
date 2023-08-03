from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define the mapping of digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index, current_combination):
            # If we've formed a combination of length equal to the digits' length
            if len(current_combination) == len(digits):
                result.append(current_combination)
                return

            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]

            # Explore all possible choices for the current digit's letters
            for letter in letters:
                # Include the current letter in the combination and move to the next digit
                backtrack(index + 1, current_combination + letter)

        result = []
        backtrack(0, "")
        return result
s=Solution()

# Testcase 1:
print(s.letterCombinations("23")) # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Testcase 2:
print(s.letterCombinations("")) # Output: []

# Testcase 3:
print(s.letterCombinations("2")) # Output: ["a","b","c"]