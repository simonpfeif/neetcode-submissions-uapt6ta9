class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, last, selling):
            if i >= len(prices):
                return 0
            if (i, last, selling) in dp:
                return dp[(i, last, selling)]
            
            if selling:
                dp[(i, last, selling)] = max(dfs(i + 1, last, True), prices[i] - prices[last] + dfs(i + 2, i, False))
            else:
                dp[(i, last, selling)] = max(dfs(i + 1, i, True), dfs(i + 1, last, False))
            return dp[(i, last, selling)]
            
        return max(0, dfs(0, 0, False))
