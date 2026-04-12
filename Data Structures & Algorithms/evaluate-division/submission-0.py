class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # a -> [(b, a/b)]
        for i, eq in enumerate(equations):
            u, v = eq
            adj[u].append((v, values[i]))
            adj[v].append((u, 1 / values[i]))
        print(adj)

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            
            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)

            while q:
                n, w = q.popleft()

                if n == target:
                    return w

                for nei, multi in adj[n]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, w * multi])
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]

# a/b = 4.0
# b/c = 1.0
# a*b / b*c = 3.25


