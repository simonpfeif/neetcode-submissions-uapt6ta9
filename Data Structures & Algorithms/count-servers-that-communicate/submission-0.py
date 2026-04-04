class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        seen_rows = [0] * ROWS
        seen_cols = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    seen_rows[r] += 1
                    seen_cols[c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (seen_rows[r] > 1 or seen_cols[c] > 1):
                    res += 1

        return res