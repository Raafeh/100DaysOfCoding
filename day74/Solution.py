class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        swap = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                swap.append(s[i])
                swap.append(goal[i])

        if len(diff) != 2:
            return False

        return swap[0] == swap[3] and swap[1] == swap[2]
# Test Cases:

solution = Solution()
print(solution.buddyStrings("ab", "ba"))  # Output: True
print(solution.buddyStrings("ab", "ab"))  # Output: False
print(solution.buddyStrings("aa", "aa"))  # Output: True
