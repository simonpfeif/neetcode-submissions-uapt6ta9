class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        t = 0

        while minHeap:

            while minHeap[0][0] <= t:
                lvl, r, c = heapq.heappop(minHeap)
                if (r, c) in visit:
                    continue

                if r == ROWS - 1 and c == COLS - 1:
                    return t

                visit.add((r, c))

                if r + 1 < ROWS: heapq.heappush(minHeap, (grid[r + 1][c], r + 1, c))
                if r - 1 >= 0: heapq.heappush(minHeap, (grid[r - 1][c], r - 1, c))
                if c + 1 < COLS: heapq.heappush(minHeap, (grid[r][c + 1], r, c + 1))
                if c - 1 >= 0: heapq.heappush(minHeap, (grid[r][c - 1], r, c - 1))


            t += 1

        return t
