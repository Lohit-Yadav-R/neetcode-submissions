class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges) + 1
        parent = [-1] * size

        def find(n):
            if parent[n] < 0:
                return n
            parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            rootn1 = find(n1)
            rootn2 = find(n2)

            if rootn1 == rootn2:
                return False
            
            if parent[rootn2] < parent[rootn1]:
                rootn1, rootn2 = rootn2, rootn1
            
            parent[rootn1] += parent[rootn2]
            parent[rootn2] = rootn1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]