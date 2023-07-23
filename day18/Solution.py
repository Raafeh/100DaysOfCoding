class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Base case: n must be odd and non-negative
        if n <= 0 or n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        result = []
        # Try all possible left and right subtree combinations
        for i in range(1, n, 2):
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(n - i - 1)

            # Create trees by combining left and right subtrees
            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result

s=Solution()

# Testcase 1
num = 7
r = s.allPossibleFBT(num)
for tree in r:
    pass

# Testcase 2
num = 1
r = s.allPossibleFBT(num)
for tree in r:
    pass



# Example usage:
# n = 7
# solution = Solution()
# result = solution.allPossibleFBT(n)
# for tree in result:
#     # Perform tree traversal to visualize the trees if needed
#     pass
