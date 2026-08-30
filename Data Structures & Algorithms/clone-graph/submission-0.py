"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        oldtonew = {}
        oldtonew[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in oldtonew:
                    copy = Node(nei.val)
                    oldtonew[nei] = copy
                    queue.append(nei)
                oldtonew[cur].neighbors.append(oldtonew[nei])
        
        return oldtonew[node]
