class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop to get val to counts mapping O(n)
        cnts = Counter(nums) # val -> count

        # Option 2:
        # maintain a max heap of size k with pairs (count, val)
        heap = []

        # loop through cnts and append to heap O(nlogn)
        for val, cnt in cnts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, val))
            elif heap[0][0] < cnt:
                heapq.heappop(heap)
                heapq.heappush(heap, (cnt, val))
        
        
        # get top k vals O(k)
        return [val for _, val in heap]

        
        # Option 1:
        # loop to get counts to val mapping O(n)

        # loop again to make counts a list O(n)

        # sort counts O(nlogn)

        # get top k vals O(k)