class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            # Convert the number to 0-based index for mapping to letters
            columnNumber -= 1
            # Get the remainder after dividing by 26
            remainder = columnNumber % 26
            # Convert the remainder to the corresponding letter
            result = chr(remainder + ord('A')) + result
            # Divide the columnNumber by 26 for the next iteration
            columnNumber //= 26
        return result

s=Solution()

# Testcase 1:
print(s.convertToTitle(1))
# Output: "A"

# Testcase 2:
print(s.convertToTitle(28))
# Output: "AB"

# Testcase 3:
print(s.convertToTitle(701))
# Output: "ZY"