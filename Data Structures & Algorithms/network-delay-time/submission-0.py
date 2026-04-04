class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w_curr, u_curr = heapq.heappop(minHeap)
            if u_curr in visit:
                continue
            visit.add(u_curr)
            t = w_curr

            for v, w in adj[u_curr]:
                if v not in visit:
                    heapq.heappush(minHeap, (w + w_curr , v))

        return t if len(visit) == n else -1