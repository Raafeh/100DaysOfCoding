# Count Valid Pickup and Delivery Sequences

## Problem Description

Given `n` orders, each consisting of a pickup and delivery service, we need to count all valid sequences where delivery(i) always occurs after pickup(i). In other words, we want to arrange the orders in such a way that the delivery for each order comes after its corresponding pickup.

### Example

For `n = 2`, the correct solution counts 6 valid sequences, as explained below:
- (P1, P2, D1, D2)
- (P1, P2, D2, D1)
- (P1, D1, P2, D2)
- (P2, P1, D1, D2)
- (P2, P1, D2, D1)
- (P2, D2, P1, D1)

## Approch and Solution

We use the following formula to efficiently calculate the number of valid sequences:

- `MOD` is set to 10^9 + 7 to ensure the result is modulo this value.
- We initialize `count` as 1 because there is only one way to arrange the first pickup and delivery.
- We then use a loop to calculate `count` for `n` pairs of pickup and delivery units, where `i` represents the number of pairs.
- The formula updates `count` efficiently by multiplying it with `(2 * i - 1) * i` and taking the modulo operation.

This solution is efficient and provides the correct answer even for large values of `n` while taking into account the modulo operation to prevent overflow.


- Time Complexity: The code runs in O(n) time complexity because it iterates through a loop of size `n`.
- Space Complexity: The code uses a constant amount of space, so it has O(1) space complexity.

Feel free to explore the repository and adapt the solution to your specific needs. Happy Coding!
