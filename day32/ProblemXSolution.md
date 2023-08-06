# Number of Music Playlist

## Problem Description

You have a music player containing `n` different songs, and you want to listen to exactly `goal` songs (not necessarily different) during your trip. However, to avoid boredom, you decide to create a playlist with the following rules:

1. Every song must be played at least once.
2. A song can only be played again if `k` other songs have been played in between.

Your task is to find the number of possible playlists you can create that adhere to these rules. Since the answer can be very large, you should return it modulo 10^9 + 7.

## Example

### Input

```python
n = 3
goal = 3
k = 1
```

### Output

```
6
```

Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

## Solution

To solve this problem, we can use dynamic programming. We'll define a 2D array `dp`, where `dp[i][j]` represents the number of possible playlists with `i` unique songs and a total length of `j`. We'll iterate over the `dp` array to fill it up using the following recurrence relation:

```
dp[i][j] = dp[i-1][j-1] * (n-i+1)    (for playing a new song, there are (n-i+1) choices)
          + dp[i][j-1] * max(i-k, 0) (for playing a song again, there are max(i-k, 0) choices)
```

The base case will be `dp[0][0] = 1`, as there's one way to create an empty playlist with no songs.

Once we have filled up the `dp` array, the answer to the problem will be stored in `dp[n][goal]`, as it represents the number of playlists with `n` unique songs and a total length of `goal`.

## Time and Space Complexity

The time complexity of the solution is O(n * goal) since we have a nested loop to fill up the `dp` array.

The space complexity is O(n * goal) as well since we use a 2D array of that size to store the dynamic programming results.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!