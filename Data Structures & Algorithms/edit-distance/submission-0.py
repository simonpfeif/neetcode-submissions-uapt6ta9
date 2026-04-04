class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    res = min(dp[i + 1][j], dp[i][j + 1])
                    dp[i][j] = 1 + min(res, dp[i + 1][j + 1])
        return dp[0][0]

        # def dfs(i, j):
        #     if i == m:
        #         return n - j
        #     if j == n:
        #         return m - i

        #     if word1[i] == word2[j]:
        #         return dfs(i + 1, j + 1)
        #     res = min(dfs(i + 1, j), dfs(i, j + 1))
        #     res = min(res, dfs(i + 1, j + 1))
        #     return res + 1
        
        # return dfs(0,0)
                
            