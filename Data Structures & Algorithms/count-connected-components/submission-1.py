class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n

        def find(node):
            if parent[node] < 0:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return
            
            if parent[root2] < parent[root1]:
                root1, root2 = root2, root1
            
            parent[root1] += parent[root2]
            parent[root2] = root1
        
        for node1, node2 in edges:
            union(node1, node2)
        
        res = 0
        for _ in parent:
            if _ < 0:
                res += 1
        
        return res