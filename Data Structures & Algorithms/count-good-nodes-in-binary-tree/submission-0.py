# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.greatest = float("-Inf")
        self.count = 0

        def dfs(root):
            if not root:
                return
            
            if root.val >= self.greatest:
                self.greatest = root.val
                self.count += 1
            
            temp = self.greatest
            
            dfs(root.left)

            self.greatest = temp

            dfs(root.right)

            return

        dfs(root)

        return self.count



        
