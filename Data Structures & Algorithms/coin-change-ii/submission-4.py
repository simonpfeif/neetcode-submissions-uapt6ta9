class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1
            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp
        return dp[amount]




        # coins.sort()
        # def dfs(i, curr):
        #     if curr == 0:
        #         return 1
        #     if i >= len(coins):
        #         return 0
            
        #     res = 0
        #     if curr >= coins[i]:
        #         res = dfs(i + 1, curr)
        #         res += dfs(i, curr - coins[i])
        #     return res
        
        # return dfs(0, amount)



