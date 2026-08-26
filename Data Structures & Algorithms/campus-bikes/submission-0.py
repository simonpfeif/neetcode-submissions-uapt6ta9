class Solution:
    def getDist(self, pair1, pair2):
        return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        closest_bikes = []
        min_heap = []
        
        for i, worker in enumerate(workers):
            cur_closest_bikes = []
            for j, bike in enumerate(bikes):
                d = self.getDist(worker, bike)
                cur_closest_bikes.append((d, i, j))
            
            cur_closest_bikes.sort(reverse=True)
            heapq.heappush(min_heap, cur_closest_bikes.pop())
            closest_bikes.append(cur_closest_bikes)

        res = [-1] * len(workers)
        seen_bike = [False] * len(bikes)
        while min_heap:
            d, worker, bike = heapq.heappop(min_heap)
            if not seen_bike[bike]:
                res[worker] = bike
                seen_bike[bike] = True
            else:
                heapq.heappush(min_heap, closest_bikes[worker].pop())
        return res


        # Approach 1
        # iterate through every combination of worker and bike
        # add each to a heap
        # pop from heap until n workers have been seen

        # Approach 2
        # iterate through every combination of workers and bikes
        # maintain a sorted list of the closest bikes for each work
        # add the closest bike to a min_heap for each worker
        # while the heap is not empty
        #   add the bike to a respective worker or add the next bike