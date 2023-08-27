# Frog River Crossing Problem

## Problem Description

The Frog River Crossing problem involves a frog trying to cross a river by jumping on stones. The river is divided into units, with some stones placed at specific unit positions. The frog can jump on a stone but must avoid jumping into the water. The goal is to determine if the frog can successfully jump on the stones and reach the last stone to cross the river.

The frog has the following rules for jumping:

- The first jump must be 1 unit.
- If the frog's last jump was of size `k` units, its next jump must be either `k - 1`, `k`, or `k + 1` units.
- The frog can only jump in the forward direction.

### Example

**Input:**
```
stones = [0, 1, 3, 5, 6, 8, 12, 17]
```

**Output:**
```
true
```

**Explanation:**
The frog can jump to the last stone by following these jumps:
1. Jump 1 unit to the 2nd stone.
2. Jump 2 units to the 3rd stone.
3. Jump 2 units to the 4th stone.
4. Jump 3 units to the 6th stone.
5. Jump 4 units to the 7th stone.
6. Jump 5 units to the 8th stone.

## Approach and Solution 

The solution involves using dynamic programming to track the possible jump sizes for each stone. We create a dictionary `jump_options`, where the keys represent stone positions, and the values are sets of possible jump sizes from that stone.

1. Initialize the jump options for the first stone with a jump size of 0.
2. Iterate through each stone and each possible jump size for that stone.
3. For each possible jump size, check if the frog can jump from the current stone to the next stone using the allowed jump sizes. If so, update the jump options for the next stone.
4. Finally, check if the last stone has any valid jump options. If it does, the frog can successfully cross the river.

### Time Complexity

The time complexity of this solution depends on the number of stones `n` and the maximum number of jump sizes `m`. The worst-case scenario occurs when the frog can potentially make all `m` jump sizes from each stone. In that case, the time complexity is approximately O(n * m^2).

### Space Complexity

The space complexity is determined by the storage of jump options for each stone. In the worst case, the frog can make all `m` jump sizes from each stone, leading to a space complexity of approximately O(n * m).

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!