class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for node in adj[curr]:
                if node == prev:
                    continue
                if not dfs(node, curr): return False
            return True

        
        return dfs(0, -1) and len(visited) == n




        # 0
       #1  2   3
    # 4


#       0
#     1
#   2
#       3