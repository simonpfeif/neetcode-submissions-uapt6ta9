class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)

        for u, v in relations:
            adj[u].append(v)
            in_degree[v] += 1

        q = deque([crs for crs in range(1, n + 1) if in_degree[crs] == 0])
        res = 0
        num_courses = 0

        while q:
            for _ in range(len(q)):
                course = q.popleft()
                num_courses += 1

                for next_crs in adj[course]:
                    in_degree[next_crs] -= 1
                    if in_degree[next_crs] == 0:
                        q.append(next_crs)
            res += 1

        return res if num_courses == n else -1
        