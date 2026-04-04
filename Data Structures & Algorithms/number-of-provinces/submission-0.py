class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for nei in range(n):
                if isConnected[node][nei] and not visited[nei]:
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                res += 1
        return res
            