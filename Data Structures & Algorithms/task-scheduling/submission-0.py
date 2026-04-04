class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        
        heapq.heapify(maxheap)
        queue = deque() # pairs of -c and time
        time = 0

        while maxheap or queue:
            time += 1

            if maxheap:
                cnt = heapq.heappop(maxheap) + 1 # dec count
                if cnt: # add to queue
                    queue.append([cnt, time + n])
            else:
                time = queue[0][1]
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
            
        return time