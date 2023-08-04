# Letter Combinations of a Phone Number

## Problem Description

Given a string containing digits from 2 to 9 (inclusive), we are required to find all possible letter combinations that the number could represent, similar to the letter combinations found on a telephone keypad. We are to return the answer in any order.

The mapping of digits to letters is as follows:

```
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
```

### Example

**Input:**
```
digits = "23"
```

**Output:**
```
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

**Input:**
```
digits = ""
```

**Output:**
```
[]
```

**Input:**
```
digits = "2"
```

**Output:**
```
["a", "b", "c"]
```

## Approach and Solution

To solve this problem, we use a recursive approach with backtracking. We start by defining a mapping of digits to their corresponding letters. Then, we create a helper function called `backtrack` that explores all possible letter combinations by iterating through the digits and their corresponding letters. The function keeps track of the current combination being formed and recursively generates all possible choices for each digit's letters. When the length of the current combination equals the length of the input digits, we add it to the final result list.

### Time and Space Complexity

The time complexity of the solution is O(4^n) where n is the number of digits in the input. This is because each digit can have a maximum of 4 letters associated with it (e.g., '7' can have 'p', 'q', 'r', and 's').

The space complexity is O(n), where n is the number of digits in the input. This is due to the recursion stack used during the backtracking process. Additionally, the space required to store the result list is also proportional to n.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!