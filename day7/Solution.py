from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        color=[0]*n
        def safe(x):
            if color[x]>0:
                return color[x]==2
            color[x]=1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x]=2
            return True
        return [i for i in range(n) if safe(i)]

s=Solution()

# Test case 1
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))

# Test case 2
print(s.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))

    