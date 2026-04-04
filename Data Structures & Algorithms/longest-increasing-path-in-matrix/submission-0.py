class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(row, col):
            res = 1
            for d in directions:
                r, c = row + d[0], col + d[1]

                if (r < ROWS and c < COLS and 
                    r >= 0 and c >= 0 and 
                    matrix[row][col] < matrix[r][c]):

                    res = max(res, 1 + dfs(r, c))
            return res
        
        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c))
        return LIP