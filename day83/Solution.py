class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)

        return ''.join(stack)

S = Solution()

# Testcase 1:
print(S.removeDuplicateLetters("bcabc")) # abc

# Testcase 2:
print(S.removeDuplicateLetters("cbacdcbc")) # acdb

