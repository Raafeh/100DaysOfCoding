# Asteroid Collision

## Problem Description

You are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Your task is to find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

### Examples

#### Example 1:

Input: `[5, 10, -5]`

Output: `[5, 10]`

Explanation: The asteroid with size 10 and the asteroid with size -5 collide resulting in the asteroid with size 10. The asteroid with size 5 and the asteroid with size 10 never collide.

#### Example 2:

Input: `[8, -8]`

Output: `[]`

Explanation: The asteroid with size 8 and the asteroid with size -8 collide, exploding each other.

#### Example 3:

Input: `[10, 2, -5]`

Output: `[10]`

Explanation: The asteroid with size 2 and the asteroid with size -5 collide resulting in the asteroid with size -5. The asteroid with size 10 and the asteroid with size -5 collide resulting in the asteroid with size 10.

## Approach and Solution

To solve this problem, we use a stack to simulate the collisions between asteroids. We iterate through the given `asteroids` array and keep track of the asteroids that haven't collided yet. When we encounter a new asteroid, we compare its direction with the top asteroid in the stack to determine if they will collide or not. If they collide, we apply the collision rules and continue checking with the remaining asteroids.

1. Create an empty stack to store the asteroids that haven't collided yet.
2. Iterate through each asteroid in the `asteroids` array.
3. For each asteroid, compare its direction with the top asteroid in the stack.
   - If the current asteroid is moving left (negative) and the top asteroid in the stack is moving right (positive), they will collide.
   - If the absolute value of the current asteroid is greater than the top asteroid, the top asteroid will explode, and we pop it from the stack.
   - If the absolute value of the current asteroid is equal to the top asteroid, both asteroids will explode, and we pop the top asteroid from the stack.
   - If the absolute value of the current asteroid is smaller than the top asteroid, the current asteroid will explode, and we break the loop.
   - If there is no collision, we simply push the current asteroid into the stack.
4. After processing all the asteroids, the stack will contain the asteroids that haven't collided yet, representing the state of the asteroids after all collisions.

The time complexity of this solution is O(n), where n is the number of elements in the `asteroids` array. We iterate through the array once, and each element is pushed and popped from the stack at most once.

The space complexity of this solution is O(n), where n is the number of elements in the `asteroids` array. The stack can potentially hold all elements if they don't collide and are not destroyed.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!