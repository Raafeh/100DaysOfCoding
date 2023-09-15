from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        n = len(points)
        edges = []  # List to store edges (cost, u, v)
        
        # Calculate the Manhattan distance between all pairs of points and store them as edges
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        
        # Sort edges by cost in ascending order
        edges.sort()
        
        parent = list(range(n))  # Initialize each point as its own parent
        min_cost = 0
        
        for cost, u, v in edges:
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                min_cost += cost
                
        return min_cost
s = Solution()

# Testcase 1:
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
# Output: 20

# Testcase 2:
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
# Output: 18
