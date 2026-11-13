class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # initialize window
        window = Counter(nums[:k])
        max_heap = [-num for num in nums[:k]]
        heapq.heapify(max_heap)
        res = [-max_heap[0]]

        l = 0
        for r in range(k, len(nums)):
            window[nums[l]] -= 1
            l += 1
            window[nums[r]] += 1
            heapq.heappush(max_heap, -nums[r])

            while window[-max_heap[0]] == 0:
                heapq.heappop(max_heap)

            res.append(-max_heap[0])
        
        return res

