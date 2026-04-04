class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            
            q.append((r, c))
            grid[r][c] = -1

            for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc)
            
        
        # Find first island
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    #populate q
                    dfs(r, c)
                    found = True
                    break
            if found: break
        

        # bfs from first island to second
        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1:
                        continue
                    elif grid[nr][nc] == 1:
                        return res
                    else:
                        q.append((nr,nc))
                        grid[nr][nc] = -1
            
            res += 1

        return res