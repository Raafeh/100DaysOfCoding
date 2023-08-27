# Course Schedule

## Problem Description

You are given a total of `numCourses` courses labeled from `0` to `numCourses - 1`. Each course has a list of prerequisites that must be completed before taking that course. Your task is to determine if it's possible to finish all the courses.

## Example

Input:
```
numCourses = 2
prerequisites = [[1,0]]
```

Output:
```
True
```

Explanation:
There are two courses to take. To take course 1, you need to finish course 0 first. Since there are no circular dependencies, it is possible to finish all courses.

Input:
```
numCourses = 2
prerequisites = [[1,0], [0,1]]
```

Output:
```
False
```

Explanation:
There are two courses to take. To take course 1, you need to finish course 0 first, and to take course 0, you need to finish course 1. This forms a cycle, and it is impossible to finish all courses.

## Approach and Solution

The problem can be solved using a graph-based approach. We can represent the courses and their prerequisites as a directed graph, where each course is a node and each prerequisite is a directed edge from one course to another.

To determine if it's possible to finish all courses, we need to check if there is any cycle in the graph. If there is a cycle, it means there is a circular dependency between courses, and it would be impossible to finish all of them.

We can solve this problem using a depth-first search (DFS) algorithm. The idea is to traverse the graph starting from each course and check for cycles. If we encounter a node that is already being visited during the traversal, it means there is a cycle, and we return `False`. If we traverse all courses without encountering any cycles, we return `True`.

The algorithm can be summarized as follows:

1. Build the adjacency list representation of the graph based on the prerequisites.
2. Initialize a `visited` list to keep track of the visited nodes during the DFS.
3. Define a recursive function `hasCycle` that takes a course as input and performs a DFS to check for cycles.
   - If the course is marked as visiting (indicating a cycle), return `True`.
   - If the course is marked as visited (indicating it has been explored without finding a cycle), return `False`.
   - Mark the course as visiting.
   - Recursively call `hasCycle` for each prerequisite course.
   - Mark the course as visited.
   - Return `False` (no cycle found).
4. Iterate over all courses and check for cycles using the `hasCycle` function.
   - If a cycle is found, return `False`.
5. If no cycles are found in any course, return `True`.

The time complexity of this solution is O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges). Building the graph takes O(E) time, and the DFS algorithm visits each node and its outgoing edges exactly once, resulting in a total time complexity of O(V + E).

The space complexity is O(V), where V is the number of courses. The graph is represented using an adjacency list, which requires O(V + E) space. Additionally, the `visited` list and the function call stack for the DFS require O(V) space.

Overall, the solution is efficient and can handle the given constraints of 1 <= numCourses <= 2000 and 0 <= prerequisites.length <= 5000.
