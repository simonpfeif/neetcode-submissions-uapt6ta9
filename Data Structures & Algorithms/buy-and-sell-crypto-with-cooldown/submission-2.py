class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, last, selling):
            if i >= len(prices):
                return 0
            
            if selling:
                return max(dfs(i + 1, last, True), prices[i] - prices[last] + dfs(i + 2, i, False))
            else:
                return max(dfs(i + 1, i, True), dfs(i + 1, last, False))
            
        return max(0, dfs(0, 0, False))
