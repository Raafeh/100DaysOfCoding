# Count Good Pairs

## Problem Description

Given an array of integers `nums`, you need to return the number of good pairs. A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

### Example:

**Input**:
```
nums = [1, 2, 3, 1, 1, 3]
```

**Output**:
```
4
```

**Explanation**:
There are 4 good pairs: (0,3), (0,4), (3,4), (2,5) (0-indexed).

## Approach and Solution

We can solve this problem efficiently using a Python function that employs a dictionary to count the occurrences of each number in the input array. The steps of the solution are as follows:

1. Initialize an empty dictionary `count_dict` to store the count of each number.
2. Initialize a variable `good_pairs` to keep track of the count of good pairs.
3. Iterate through the input array `nums` and for each number `num`, do the following:
   - If `num` is already in `count_dict`, increment its count by 1.
   - If `num` is not in `count_dict`, add it to the dictionary with a count of 1.
4. After counting the occurrences of each number, iterate through the values in `count_dict` and calculate the number of good pairs for each number using the formula `(count * (count - 1)) // 2`, where `count` is the number of occurrences of that number.
5. Add up the counts of good pairs for all numbers in `count_dict` to get the total count of good pairs in the array.
6. Return the `good_pairs` count as the final result.

### Time Complexity

The time complexity of this solution is O(N), where N is the number of elements in the input array `nums`. This is because we iterate through the array once to count the occurrences of each number, and then we iterate through the values in the dictionary, which has at most N unique elements.

### Space Complexity

The space complexity of this solution is O(N), where N is the number of unique elements in the input array `nums`. This is because we use a dictionary `count_dict` to store the counts of each unique number in the array, and in the worst case, there can be N unique numbers.
