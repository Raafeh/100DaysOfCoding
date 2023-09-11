# Group the People Given the Group Size

## Problem Description

You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the group that person i is in. Your task is to group these people according to their group size while ensuring that each person is in a group of the specified size. There may be multiple valid solutions for the given input, and you need to return one of them.

**Input:**
- An integer array `groupSizes` (1 ≤ `groupSizes.length` ≤ 500)
- `groupSizes[i]` is an integer representing the size of the group that person i is in.

**Output:**
- A list of groups such that each person is in a group of the specified size.

## Example

### Example 1

**Input:** 
```python
groupSizes = [3, 3, 3, 3, 3, 1, 3]
```

**Output:**
```python
[[5], [0, 1, 2], [3, 4, 6]]
```

**Explanation:**
- The first group is [5]. The size is 1, and `groupSizes[5] = 1`.
- The second group is [0, 1, 2]. The size is 3, and `groupSizes[0] = groupSizes[1] = groupSizes[2] = 3`.
- The third group is [3, 4, 6]. The size is 3, and `groupSizes[3] = groupSizes[4] = groupSizes[6] = 3`.
- Other possible solutions are `[[2, 1, 6], [5], [0, 4, 3]]` and `[[5], [0, 6, 2], [4, 3, 1]]`.

### Example 2

**Input:** 
```python
groupSizes = [2, 1, 3, 3, 3, 2]
```

**Output:**
```python
[[1], [0, 5], [2, 3, 4]]
```

## Approach and Solution

To solve this problem, we can use the following algorithm:

1. Initialize a dictionary (`groups`) to store people by their group size.

2. Populate the dictionary by iterating through the `groupSizes` array. For each person, we check their group size and add them to the corresponding list in the dictionary.

3. Create an empty list (`result`) to store the final groups.

4. Iterate through the dictionary to form groups. For each group size, we repeatedly pop elements from the corresponding list until it is empty or the group size is reached. We append these groups to the `result` list.

5. Return the `result` list as the final solution.

### Time Complexity

The time complexity of this solution is O(n), where n is the number of people.

### Space Complexity

The space complexity of this solution is O(n) since we store the people in the `groups` dictionary.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
