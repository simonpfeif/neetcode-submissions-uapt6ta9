class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return
            
            grid[r][c] = 0

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        res = 0
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                res += grid[r][c]
        
        return res