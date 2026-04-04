class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]

        q = deque()
        time = 0
        while maxheap or q:
            time += 1

            if maxheap:
                cnt = -heapq.heappop(maxheap) - 1

                if cnt > 0:
                    q.append((cnt, time + n))
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxheap, -q[0][0])
                q.popleft()

        return time
