class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

        # cache = [[-1] * n for _ in range(m)]

        # def dfs(r, c):
        #     if r == (m - 1) and c == (n - 1):
        #         return 1
        #     elif r >= m or c >= n:
        #         return 0
        #     if cache[r][c] == -1:            
        #         cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[r][c]
        
        # return dfs(0, 0)
        

        # n = 2 [0][1]