class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}

        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visit = set()
        minHeap = [(0, 0)]
        res = 0
        while len(visit) < N:
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
                
            visit.add(point)
            res += dist

            for d, p in adj[point]:
                if p not in visit:
                    heapq.heappush(minHeap, (d, p))
        return res