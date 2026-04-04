class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            rock1 = -heapq.heappop(heap)
            rock2 = -heapq.heappop(heap)
            rock3 = rock1 - rock2
            if rock3 > 0:
                heapq.heappush(heap, -rock3)
        heap.append(0)
        return -heap[0]