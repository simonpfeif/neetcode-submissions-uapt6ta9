class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0] = costs[0]

        for i in range(1, n):
            for c in range(3):
                
                dp[i][c] = costs[i][c] + min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3])
        
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])

        # def dfs(i, last):
        #     if i == n:
        #         return 0
            
        #     res = float('inf')
        #     for j in range(3):
        #         if last == j:
        #             continue
        #         res = min(res, costs[i][j] + dfs(i + 1, j))
            
        #     return res
        
        # return dfs(0, -1)