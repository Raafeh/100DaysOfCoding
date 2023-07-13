from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            course, prerequisite_course = prerequisite
            graph[course].append(prerequisite_course)

        visited = [0] * numCourses  # 0 = Not visited, 1 = Visiting, 2 = Visited

        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1  # Mark as visiting

            for prerequisite_course in graph[course]:
                if hasCycle(prerequisite_course):
                    return True

            visited[course] = 2  # Mark as visited
            return False

        # Check for cycles in each course
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True
    
s=Solution()
# Test Case 1:
print(s.canFinish(2, [[1,0]]))

# Test Case 2:
print(s.canFinish(2, [[1,0],[0,1]]))
