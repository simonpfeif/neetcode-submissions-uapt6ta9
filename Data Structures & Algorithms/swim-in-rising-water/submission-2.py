class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        t = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == ROWS - 1 and c == COLS - 1:
                return t
            
            for dr, dc in directions:
                rn, cn = r + dr, c + dc
                if rn < 0 or rn >= ROWS or cn < 0 or cn >= COLS or (rn, cn) in visit:
                    continue

                visit.add((rn, cn))
                heapq.heappush(minHeap, (max(t, grid[rn][cn]), rn, cn))

        return t
