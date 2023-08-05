# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        
        def generate_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left_subtrees = generate_trees(start, i - 1)
                right_subtrees = generate_trees(i + 1, end)
                
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        all_trees.append(root)
            
            return all_trees
        
        return generate_trees(1, n)
    
s=Solution()

# Testcase 1:
print(s.generateTrees(3))

# Testcase 2:
print(s.generateTrees(1))

# Testcase 3:
print(s.generateTrees(0))