class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        def dfs(node, visit):
            if node == destination and len(adj[node]) == 0:
                return True
            
            if node in visit or len(adj[node]) == 0:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei, visit):
                    return False
            
            visit.remove(node)
            return True
        

        return dfs(source, set())