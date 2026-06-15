class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = costs[0]

        for i in range(1, n):
            nxt_dp = [float('inf')] * 3
            for c in range(3):
                
                nxt_dp[c] = costs[i][c] + min(dp[(c + 1) % 3], dp[(c + 2) % 3])
            dp = nxt_dp
        
        return min(dp[0], dp[1], dp[2])

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