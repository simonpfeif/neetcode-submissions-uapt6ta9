class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)] # w is the key, node is the "val"
        t = 0
        visit = set()

        while minHeap:
            curr_weight, curr = heapq.heappop(minHeap)
            if curr in visit:
                continue
            
            t = curr_weight
            visit.add(curr)

            for node, w in adj[curr]:
                if node not in visit:
                    heapq.heappush(minHeap, (w + t, node))

        return t if n == len(visit) else -1
