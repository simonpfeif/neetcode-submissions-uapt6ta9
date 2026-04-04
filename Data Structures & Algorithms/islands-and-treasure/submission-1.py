class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque() # append and pop left

        # find all land
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            print("q front: ", q[0])
            r, c = q.popleft()
            for d in directions:
                row = d[0] + r
                col = d[1] + c
                print(row, col)

                if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] != INF:
                    continue
                print(row, col)
                grid[row][col] = grid[r][c] + 1
                q.append((row, col))
