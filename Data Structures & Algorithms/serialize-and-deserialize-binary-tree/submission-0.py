# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if not root:
                res.append('#')
                return
            
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ','.join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(',')
        self.index = 0
        def reconstruct():
            if self.index == len(tokens):
                return
            if tokens[self.index] == '#':
                return None
            
            root = TreeNode(tokens[self.index])
            self.index += 1
            root.left = reconstruct()
            self.index += 1
            root.right = reconstruct()

            return root
        
        root = reconstruct()

        return root

















