class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        
        def totalways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            if i in memo:
                return memo[i]
            
            memo[i] = (k - 1) * (totalways(i - 1) + totalways(i - 2))
        
            return memo[i]
        
        return totalways(n)