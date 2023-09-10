
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        count = 1 
        for i in range(2, n + 1):
            count = (count * (2 * i - 1) * i) % MOD
        return count
    
s = Solution()

# Testcase 1:
print(s.countOrders(1))
# Output: 1

# Testcase 2:
print(s.countOrders(2))
# Output: 6

# Testcase 3:
print(s.countOrders(3))
# Output: 90