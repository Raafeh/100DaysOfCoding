# Pow(x, n)

## Problem Description

You are given two inputs: a floating-point number `x` and an integer `n`. Your task is to calculate `x` raised to the power `n`, denoted as `x^n`.

### Examples

Example 1:

Input: ```x = 2.00000, n = 10```

Output: ```1024.00000```

Example 2:

Input: ```x = 2.10000, n = 3```

Output: `9.26100`

Example 3:

Input: ``x = 2.00000, n = -2``

Output: `0.25000`

Explanation: ``2^(-2) = 1/2^2 = 1/4 = 0.25``


## Approach and Solution

The problem requires us to calculate the value of x raised to the power n (x^n). To solve this efficiently, we can use the concept of binary exponentiation. The binary exponentiation algorithm reduces the number of multiplication operations needed to calculate the result.

Binary exponentiation works as follows:

1. If the exponent `n` is 0, we return 1.0, as any number raised to the power 0 is 1.
2. Otherwise, we calculate half_pow by recursively calling the power function with the base and exponent divided by 2.
3. Then, we calculate the result by multiplying half_pow with itself.
4. If the exponent is odd (n % 2 == 1), we multiply the result with the base to account for the remaining power.
5. Finally, we return the result.

In the case where the exponent `n` is negative, we can take advantage of the property that x^(-n) is equal to (1/x)^n. So, we first calculate (1/x) and then change the sign of `n` to be positive. The binary exponentiation algorithm handles the rest.

### Time Complexity

The time complexity of the binary exponentiation algorithm is O(log n). This is because we are reducing the exponent by half in each recursive call, effectively dividing the problem size in half.

### Space Complexity

The space complexity of the binary exponentiation algorithm is O(log n) as well. This is due to the recursive nature of the solution, which creates a stack frame for each recursive call. Since we make O(log n) recursive calls, the space complexity is O(log n).

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!