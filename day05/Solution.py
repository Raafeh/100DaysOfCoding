from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return Solution().minDepth(root.right) + 1

        if root.right is None:
            return Solution().minDepth(root.left) + 1

        left_depth = Solution().minDepth(root.left)
        right_depth = Solution().minDepth(root.right)
        return min(left_depth, right_depth) + 1
    
s=Solution()

# Test Case:1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right=TreeNode(7)
print(s.minDepth(root)) # Solution= 2

# Test Case:2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(s.minDepth(root)) # Solution= 5