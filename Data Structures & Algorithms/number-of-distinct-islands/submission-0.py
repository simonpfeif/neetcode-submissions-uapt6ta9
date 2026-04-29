class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or not grid[r][c]:
                return
            
            seen.add((r, c))
            cur.add((r - r_origin, c - c_origin))
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + x, c + y)


        islands = set()
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                cur = set()
                r_origin = r
                c_origin = c
                dfs(r, c)
                if cur:
                    islands.add(frozenset(cur))

        
        return len(islands)