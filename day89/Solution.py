class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_score = 0
        bob_score = 0

        # Count consecutive 'A's and 'B's
        count_a = 0
        count_b = 0

        for c in colors:
            if c == 'A':
                count_a += 1
                count_b = 0
                if count_a >= 3:
                    alice_score += 1
            else:
                count_b += 1
                count_a = 0
                if count_b >= 3:
                    bob_score += 1

        # Determine the winner
        if alice_score > bob_score:
            return True
        else:
            return False

s = Solution()

# Testcase 1:
print(s.winnerOfGame("AAABABB")) # True

# Testcase 2:
print(s.winnerOfGame("AA")) # False

# Testcase 3:
print(s.winnerOfGame("ABAB")) # False

