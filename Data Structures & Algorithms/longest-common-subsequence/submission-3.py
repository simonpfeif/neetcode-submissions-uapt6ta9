class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]


        # memo = {}
        
        # def dfs(l, r):
        #     if l >= len(text1) or r >= len(text2):
        #         return 0
        #     if (l, r) in memo:
        #         return memo[(l, r)]

        #     if text1[l] == text2[r]:
        #         memo[(l, r)] = 1 + dfs(l + 1, r + 1)
        #     else:
        #         memo[(l, r)] = max(dfs(l + 1, r), dfs(l, r + 1))
            
        #     return memo[(l, r)]
            
        # return dfs(0, 0)