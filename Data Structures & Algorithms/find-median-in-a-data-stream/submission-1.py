class MedianFinder:

    def __init__(self):
        self.minRightHeap = []
        self.maxLeftHeap = []

    def addNum(self, num: int) -> None:
        if self.minRightHeap and num < self.minRightHeap[0]:
            # add to left heap
            heapq.heappush(self.maxLeftHeap, -1 * num)
            print("here1")
            print(num)
        else:
            # no elements yet or add to right heap
            heapq.heappush(self.minRightHeap, num)
            print("here2")
            print(num)
    
        # rebalance
        if len(self.maxLeftHeap) > len(self.minRightHeap) + 1:
            val = -1 * heapq.heappop(self.maxLeftHeap)
            heapq.heappush(self.minRightHeap, val)
        if len(self.minRightHeap) > len(self.maxLeftHeap) + 1:
            val = heapq.heappop(self.minRightHeap)
            heapq.heappush(self.maxLeftHeap, -1 * val)
        
            

    def findMedian(self) -> float:
        if len(self.minRightHeap) < len(self.maxLeftHeap):
            return -1 * self.maxLeftHeap[0]
        elif len(self.minRightHeap) > len(self.maxLeftHeap):
            return self.minRightHeap[0]
        else:
            return (self.minRightHeap[0] + -1 * self.maxLeftHeap[0]) / 2.0