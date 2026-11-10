class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for r in range(1, len(prices)):
            min_price = min(min_price, prices[r])
            max_profit = max(max_profit, prices[r] - min_price)
        
        return max_profit