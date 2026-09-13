class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node, prevNode = None):
            visited.add(node)
            for nextNode in adj[node]:
                if nextNode == prevNode or nextNode in visited:
                    continue
                dfs(nextNode, node)
        
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res