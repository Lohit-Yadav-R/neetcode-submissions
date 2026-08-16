# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_height_diff = 0

        def dfs(root):
            if root is None:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            self.max_height_diff = max(self.max_height_diff, abs(left_depth - right_depth))
            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.max_height_diff <= 1