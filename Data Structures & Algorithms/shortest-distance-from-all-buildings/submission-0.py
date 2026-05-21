class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # distances[r][c][0] tracks count of buildings reached
        # distances[r][c][1] tracks total cumulative distance
        distances = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]
        num_houses = 0
        
        def bfs(start_r, start_c):
            seen = [[False] * COLS for _ in range(ROWS)]
            q = deque([(start_r, start_c, 0)])
            seen[start_r][start_c] = True

            while q:
                r, c, traveled = q.popleft()

                if grid[r][c] == 0:
                    distances[r][c][0] += 1
                    distances[r][c][1] += traveled

                for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and not seen[nr][nc] and grid[nr][nc] == 0:
                        seen[nr][nc] = True
                        q.append((nr, nc, traveled + 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_houses += 1
                    bfs(r, c)

        res = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and distances[r][c][0] == num_houses:
                    res = min(res, distances[r][c][1])

        return -1 if res == float('inf') else res