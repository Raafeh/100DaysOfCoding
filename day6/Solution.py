# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Build the parent dictionary using DFS
        parent = {}

        def build_parent(node, par=None):
            if node:
                parent[node] = par
                build_parent(node.left, node)
                build_parent(node.right, node)

        build_parent(root)

        # Step 2: Perform DFS from the target node to find nodes at distance k
        result = []
        visited = set()
        
        def dfs(node, dist):
            if node and node not in visited:
                visited.add(node)
                if dist == k:
                    result.append(node.val)
                else:
                    dfs(node.left, dist + 1)
                    dfs(node.right, dist + 1)
                    dfs(parent[node], dist + 1)
            
        dfs(target, 0)
        return result
    

s=Solution()
# Test Case 1
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
target = root.left
k = 2
print(s.distanceK(root, target, k))    