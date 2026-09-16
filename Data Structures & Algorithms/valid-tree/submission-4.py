class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
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
                return False
            
            if parent[root2] < parent[root1]:
                root1, root2 = root2, root1
            
            parent[root1] += parent[root2]
            parent[root2] = root1
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return False
        
        return True