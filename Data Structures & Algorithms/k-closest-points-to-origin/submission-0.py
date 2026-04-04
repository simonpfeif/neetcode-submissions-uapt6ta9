class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, [-dist, point[0], point[1]])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for point in heap:
            res.append([point[1], point[2]])
        return res
        
        

    # heap -> dist, x, y
    # maintain size k of max heap