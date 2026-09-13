class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node, prevNode = None):
            visited.add(node)
            for nextNode in adj[node]:
                if nextNode == prevNode:
                    continue
                if nextNode in visited:
                    return False
                dfs(nextNode, node)
            return True

        return dfs(0) and len(visited) == n