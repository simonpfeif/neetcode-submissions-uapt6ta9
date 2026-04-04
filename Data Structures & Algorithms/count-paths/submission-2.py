class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == (m - 1) and c == (n - 1):
                return 1
            elif r >= m or c >= n:
                return 0
            if cache[r][c] == -1:            
                cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]
        
        return dfs(0, 0)
        