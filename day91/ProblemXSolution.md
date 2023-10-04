# Design HashMap 

## Problem Statement

The problem is to design and implement a HashMap class with the following functionalities:

1. `MyHashMap()`: Initializes an empty HashMap.
2. `put(key, value)`: Inserts a (key, value) pair into the HashMap. If the key already exists in the map, the corresponding value is updated.
3. `get(key)`: Returns the value to which the specified key is mapped, or -1 if the key is not found in the map.
4. `remove(key)`: Removes the key and its corresponding value from the map if the map contains the mapping for the key.

## Approach and Solution

The solution involves designing a custom HashMap data structure using an array of buckets. Each bucket contains a list of key-value pairs that have the same hash code. The key operations are implemented as follows:

- `put(key, value)`: 
    - Calculate the hash code of the key to determine which bucket it belongs to.
    - If the bucket does not exist, create it.
    - Iterate through the list of key-value pairs in the bucket.
    - If the key already exists in the list, update its corresponding value; otherwise, append a new key-value pair.
- `get(key)`: 
    - Calculate the hash code of the key to determine which bucket it belongs to.
    - If the bucket does not exist, return -1.
    - Iterate through the list of key-value pairs in the bucket and return the value if the key is found; otherwise, return -1.
- `remove(key)`: 
    - Calculate the hash code of the key to determine which bucket it belongs to.
    - If the bucket does not exist, do nothing.
    - Iterate through the list of key-value pairs in the bucket and remove the pair if the key matches.

### Time Complexity

The time complexity of the implemented `MyHashMap` class is as follows:
- `put(key, value)`: O(1) on average, but O(n) in the worst case if there are many hash collisions.
- `get(key)`: O(1) on average, but O(n) in the worst case if there are many hash collisions.
- `remove(key)`: O(1) on average, but O(n) in the worst case if there are many hash collisions.

### Space Complexity

The space complexity of the `MyHashMap` class is O(n), where n is the number of unique keys in the HashMap. It is primarily determined by the number of key-value pairs stored in the HashMap.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
