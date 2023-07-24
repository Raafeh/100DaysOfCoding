class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

s=Solution()
# Testcase 1:
print(s.myPow(2.00000, 10))
# Output: 1024.00000

# Testcase 2:
print(s.myPow(2.10000, 3))
# Output: 9.26100

# Testcase 3:
print(s.myPow(2.00000, -2))
# Output: 0.25000
