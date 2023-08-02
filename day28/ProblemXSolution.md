# Permutations


## Problem Description

Given an array `nums` of distinct integers, the task is to find and return all possible permutations of the elements in the array. The order of the permutations does not matter, and the solution can return the answer in any order.

### Example

**Input:**
```
nums = [1, 2, 3]
```
**Output:**
```
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
```

**Input:**
```
nums = [0, 1]
```
**Output:**
```
[[0, 1], [1, 0]]
```

**Input:**
```
nums = [1]
```
**Output:**
```
[[1]]
```

## Approach and Solution

The solution to this problem involves using a backtracking algorithm to generate all possible permutations of the input array. The backtracking algorithm explores different combinations of the elements in the array and swaps elements to generate different permutations.

The main steps of the solution are as follows:

1. Define a function `permute(nums)` that takes the input array `nums` as an argument and returns all possible permutations.
2. Inside the `permute` function, define a helper function called `backtrack(start)`. This function will be responsible for generating permutations recursively.
3. The `backtrack` function takes a parameter `start`, which represents the current position in the array that needs to be filled with an element during the permutation generation process.
4. If `start` is equal to the length of the array `nums` minus 1, it means that all elements have been placed, and we have found a valid permutation. In this case, we add the current permutation (a copy of `nums`) to the result list and return from the function.
5. Otherwise, for each index `i` from `start` to the end of the array, we swap the element at index `start` with the element at index `i`. This simulates the selection of an element at the current position in the permutation.
6. After swapping, we make a recursive call to the `backtrack` function with the updated `start`, which represents the next position to be filled in the permutation.
7. After the recursive call, we backtrack by swapping the elements back to their original positions. This is crucial for exploring other permutations correctly.
8. The `permute` function initializes an empty list `result` to store all the permutations and calls the `backtrack` function with `start=0` to start the permutation generation process.
9. Once all the permutations are generated, the function returns the `result` list containing all possible permutations of the input array.

The time complexity of the solution is O(N!), where N is the number of elements in the input array `nums`. This is because there are N! possible permutations of a set of N distinct elements, and the backtracking algorithm explores all of them.

The space complexity is O(N) due to the recursion stack used during the backtracking process. Additionally, the `result` list stores all the permutations, which can also contribute to the space complexity. However, the space used for storing the permutations is not counted in the space complexity as it is a part of the required output.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!