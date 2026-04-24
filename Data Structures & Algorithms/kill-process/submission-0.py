class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n = len(pid)
        adj = {}

        for i in range(n):
            u, v = ppid[i], pid[i]
            
            if u not in adj:
                adj[u] = []

            adj[u].append(v)

        stack = []
        stack.append(kill)
        res = []
        while stack:
            node = stack.pop()
            res.append(node)

            for nei in adj.get(node, []):
                stack.append(nei)
        
        return res