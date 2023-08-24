# Reorganize String

## Problem Statement

Given a string `s`, the goal is to rearrange its characters in a way that no two adjacent characters are the same. If such a rearrangement is possible, return any valid rearranged string; otherwise, return an empty string.

### Example

**Input:**
```
s = "aab"
```
**Output:**
```
"aba"
```
In this example, the characters 'a' and 'b' alternate, fulfilling the condition of not having adjacent repeating characters.

**Input:**
```
s = "aaab"
```
**Output:**
```
""
```
In this example, it's not possible to rearrange the characters without having adjacent repeating characters, so the output is an empty string.

## Approach and Solution 

To solve this problem, we use a max heap data structure to keep track of the characters and their frequencies in a descending order of frequency. The steps of the solution are as follows:

1. Count the frequency of each character in the input string `s`.
2. Create a max heap and add the characters along with their negative frequencies to it.
3. Pop the two characters with the highest frequencies from the heap.
4. Append these characters to the result string and decrement their counts.
5. If a character's count is still greater than 0, push it back to the heap.
6. Repeat steps 3-5 until there are only one or no characters left in the heap.
7. If a character is left in the heap, append it to the result.
8. Return the final rearranged string or an empty string if not possible.

### Time Complexity

The time complexity of the solution is primarily determined by the heap operations and the final string concatenation. The heap operations take O(n * log(n)) time, where n is the length of the input string. The final string concatenation step also takes O(n) time in the worst case. Therefore, the overall time complexity is O(n * log(n)).

### Space Complexity

The space complexity is determined by the storage of characters and their frequencies in the heap. In the worst case, all unique characters are present in the heap, which requires O(n) space. Additionally, the result string occupies O(n) space. Hence, the total space complexity is O(n).
